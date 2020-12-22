from datetime import datetime


def donustur_saat(ilk_ts, ders_ts, cik_ts):
    ilk_d = datetime.fromtimestamp(ilk_ts - 10800)
    ders_d = datetime.fromtimestamp(ders_ts - 10800)
    cik_d = datetime.fromtimestamp(cik_ts - 10800)
    return str(ilk_d).split()[1], str(ders_d).split()[1], str(cik_d).split()[1]


class ZilUret:

    def __init__(self, _ZilData, _DersZamanlama):
        self.kontrol = {'toplangun': True, 'toplan': False, 'guncount': 0, 'osderssaati': '12:00:00'}
        self.gunler = ['Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma', 'Cumartesi', 'Pazar']
        self.gziller = _ZilData.objects.all()
        self.zamanlar = _DersZamanlama
        self.sabit_saniye = datetime.timestamp(datetime(2000, 1, 1, 0, 0, 0))
        self.dveri = list()

        for x in self.gziller:
            if x.active:
                if x.zilgun in [0, 1, 2, 3, 4, 5, 6]:
                    self.veri = dict()
                    self.veri['toplanmasuresi'] = x.toplanmasuresi
                    self.veri['dersbaslangicsaati'] = x.dersbaslangicsaati
                    self.veri['ogretmenzilsuresi'] = x.ogretmenzilsuresi
                    self.veri['derssayisi'] = x.derssayisi
                    self.veri['derssuresi'] = x.derssuresi
                    self.veri['tenefussuresi'] = x.tenefussuresi
                    self.veri['oglenarasiders'] = x.oglenarasiders
                    self.veri['oglenarasisuresi'] = x.oglenarasisuresi
                    self.veri['zilgun'] = x.zilgun
                    self.veri['active'] = x.active
                    self.dveri.append(self.veri)

    def oglensonrasi(self, oglenarasisuresi, ossaat):
        oglen_saniye = self.toplam_saniye(oglenarasisuresi)
        osson_saniye = self.toplam_saniye(ossaat)
        _sure = oglen_saniye + osson_saniye
        _ders = datetime.fromtimestamp(_sure - 10800)
        self.kontrol['osderssaati'] = str(_ders).split()[1]
        return str(_ders).split()[1]

    def toplanmazaman(self, okulbaslamazaman, toplanmasuresi):
        toplan_saniye = self.toplam_saniye(okulbaslamazaman)
        tsures_saniye = self.toplam_saniye(toplanmasuresi)
        _sure = toplan_saniye - tsures_saniye
        _ders = datetime.fromtimestamp(_sure - 10800)
        return str(_ders).split()[1]

    def gunun_zili(self, z, **kwargs):
        f_veri = {}
        for key, value in kwargs.items():
            f_veri[key] = value

        ilk, ders, cik = self.derszilihesapla(z, **f_veri)
        if z == 1:
            toplanzil_saat = self.toplanmazaman(f_veri['dersbaslangicsaati'], f_veri['toplanmasuresi'])
            veri = self.zamanlar(
                okul_turu="Örgün",
                ders_gun=f_veri['zilgun'],
                ders_no=z,
                toplanma_saati=toplanzil_saat,
                ders_baslangic=ilk,
                ogretmen_saat=ders,
                ders_bitis=cik,
                active=True,
                published_date=datetime.now(),
            )
        else:
            veri = self.zamanlar(
                okul_turu="Örgün",
                ders_gun=f_veri['zilgun'],
                ders_no=z,
                toplanma_saati='00:00:00',
                ders_baslangic=ilk,
                ogretmen_saat=ders,
                ders_bitis=cik,
                active=True,
                published_date=datetime.now(),
            )
        veri.save()
        return ilk, ders, cik

    def toplam_saniye(self, sure):
        saat, dakika, saniye = str(sure).split(':')
        _tarih = datetime(2000, 1, 1, int(saat), int(dakika), 0)
        saniye = datetime.timestamp(_tarih)
        return saniye - self.sabit_saniye

    def derszilihesapla(self, z, **kwargs):
        f_veri = {}
        for key, value in kwargs.items():
            f_veri[key] = value

        oglen_dersii = f_veri['oglenarasiders']
        oglen_saniye = self.toplam_saniye(f_veri['oglenarasisuresi'])
        obast_saniye = self.toplam_saniye(f_veri['dersbaslangicsaati'])
        suret_saniye = self.toplam_saniye(f_veri['derssuresi'])
        tenft_saniye = self.toplam_saniye(f_veri['tenefussuresi'])
        ogrtt_saniye = self.toplam_saniye(f_veri['ogretmenzilsuresi'])

        if (z > oglen_dersii) and (oglen_dersii != 0 and oglen_dersii is not None):
            obast_saniye += (oglen_saniye - tenft_saniye)

        ilk = ((obast_saniye + (z - 1) * (suret_saniye + tenft_saniye)) - ogrtt_saniye)
        ders = (obast_saniye + (z - 1) * (suret_saniye + tenft_saniye))
        cik = obast_saniye + z * suret_saniye + (z - 1) * tenft_saniye

        _ilk, _ders, _cik = donustur_saat(ilk, ders, cik)

        return _ilk, _ders, _cik

    def tanimsizgun(self):
        hitanimligun = list()
        pzt_veri = dict()
        for g in self.dveri:
            if g.get('zilgun') in [0, 1, 2, 3, 4]:
                hitanimligun.append(g.get('zilgun'))

        for g in self.dveri:
            if g.get('zilgun') == 0:
                pzt_veri = g

        return pzt_veri, set(hitanimligun).symmetric_difference({0, 1, 2, 3, 4})

    def uret(self):
        try:
            pztx_veri, manup_veri = list(self.tanimsizgun())
            for g in self.dveri:
                for i in range(1, g.get('derssayisi', None) + 1):
                    if g.get('zilgun', None) in [0, 1, 2, 3, 4]:
                        ilk, ders, cik = self.gunun_zili(i, **g)
                        print("{} {}.Ders {} {} {}".format(self.gunler[g.get('zilgun', None)], i, ilk, ders, cik))
                    if g.get('zilgun', None) in [5, 6]:
                        ilk, ders, cik = self.gunun_zili(i, **g)
                        print("{} {}.Ders {} {} {}".format(self.gunler[g.get('zilgun', None)], i, ilk, ders, cik))

            for gbf in manup_veri:
                pztx_veri.update({'zilgun': gbf})
                for i in range(1, pztx_veri.get('derssayisi', None) + 1):
                    ilk, ders, cik = self.gunun_zili(i, **pztx_veri)
                    print("{} {}.Ders {} {} {}".format(self.gunler[pztx_veri.get('zilgun')], i, ilk, ders, cik))

        except TypeError:
            pass

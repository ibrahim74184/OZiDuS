
from ozilanons.models import ZilData
from ozilanons.models import DersZamanlama
from datetime import datetime, time, timedelta


class ZilUret:

    def __init__(self, _ZilData, _DersZamanlama):

        self.kontrol = {'toplangun': True, 'toplan': False, 'guncount': 0, 'osderssaati': '12:00:00'}
        self.gunler = ['Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma', 'Cumartesi', 'Pazar']
        self.gziller = _ZilData.objects.all()
        self.DersZamanlama = DersZamanlama
        self.sabit_saniye = datetime.timestamp(datetime(2000, 1, 1, 0, 0, 0))


    def oglensonrasi(self,oglenarasisuresi, ossaat):
        oglen_saniye = self.toplam_saniye(oglenarasisuresi)
        osson_saniye = self.toplam_saniye(ossaat)
        _sure = oglen_saniye + osson_saniye
        _ders = datetime.fromtimestamp(_sure - 10800)
        self.kontrol['osderssaati'] = str(_ders).split()[1]
        return str(_ders).split()[1]


    def toplanmazaman(self,okulbaslamazaman, toplanmasuresi):
        toplan_saniye = self.toplam_saniye(okulbaslamazaman)
        tsures_saniye = self.toplam_saniye(toplanmasuresi)
        _sure = toplan_saniye - tsures_saniye
        _ders = datetime.fromtimestamp(_sure - 10800)
        return str(_ders).split()[1]


    def gunun_zili(self, z, gun_id, pt_dersbaslangicsaati, pt_toplanmasuresi, pt_tenefussuresi, pt_ogretmenzilsuresi,
                   pt_derssuresi):
        if self.kontrol.get('toplangun'):
            toplanzil_saat = self.toplanmazaman(pt_dersbaslangicsaati, pt_toplanmasuresi)
            self.kontrol['toplan'] = toplanzil_saat
            print("Toplanma {}".format(toplanzil_saat))

        ilk, ders, cik = self.derszilihesapla(z, pt_dersbaslangicsaati, pt_derssuresi, pt_tenefussuresi, pt_ogretmenzilsuresi)

        veri = self._DersZamanlama(
            okul_turu="zil.okul_turu",
            ders_gun=gun_id,
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


    def donustur_saat(self, ilk_ts, ders_ts, cik_ts):
        ilk_d = datetime.fromtimestamp(ilk_ts - 10800)
        ders_d = datetime.fromtimestamp(ders_ts - 10800)
        cik_d = datetime.fromtimestamp(cik_ts - 10800)
        return str(ilk_d).split()[1], str(ders_d).split()[1], str(cik_d).split()[1]


    def derszilihesapla(self, z, dersbsaati='09:00:00', derssuresi='00:30:00', tenefussuresi='00:10:00', ogretmenzil='00:03:00'):
        obast_saniye = self.toplam_saniye(dersbsaati)
        suret_saniye = self.toplam_saniye(derssuresi)
        tenft_saniye = self.toplam_saniye(tenefussuresi)
        ogrtt_saniye = self.toplam_saniye(ogretmenzil)

        ilk = ((obast_saniye + (z - 1) * (suret_saniye + tenft_saniye)) - ogrtt_saniye)
        ders = (obast_saniye + (z - 1) * (suret_saniye + tenft_saniye))
        cik = obast_saniye + z * suret_saniye + (z - 1) * tenft_saniye

        _ilk, _ders, _cik = self.donustur_saat(ilk, ders, cik)
        return _ilk, _ders, _cik


    def defaultgunhi(self):
        hitanimligun = list()
        for x in self.gziller:
            if x.active:
                if (x.zilgun in [0, 1, 2, 3, 4]) and (x.zilgun not in [5, 6]):
                    hitanimligun.append(x.zilgun)

        hitanimsizgun = set(hitanimligun).symmetric_difference(set([0, 1, 2, 3, 4]))
        return hitanimsizgun

    def uret(self):

        for x in self.gziller:
            if x.active:
                if (x.zilgun in [0, 1, 2, 3, 4]) and (x.zilgun not in [5, 6]):
                    pt_toplanmasuresi = x.toplanmasuresi
                    pt_dersbaslangicsaati = x.dersbaslangicsaati
                    pt_ogretmenzilsuresi = x.ogretmenzilsuresi
                    pt_derssayisi = x.derssayisi
                    pt_derssuresi = x.derssuresi
                    pt_tenefussuresi = x.tenefussuresi
                    pt_oglenarasiders = x.oglenarasiders
                    pt_oglenarasisuresi = x.oglenarasisuresi
                    gun_id = x.zilgun
                    self.kontrol['toplangun'] = True
                    if pt_oglenarasiders == 0 or pt_oglenarasiders is None:
                        pt_oglenarasiders = pt_derssayisi

                    for z in range(1, pt_derssayisi + 1):
                        if z > 1:
                            self.kontrol['toplangun'] = False
                        if z <= pt_oglenarasiders:
                            ilk, ders, cik = self.gunun_zili(z, gun_id, pt_dersbaslangicsaati, pt_toplanmasuresi,
                                                             pt_tenefussuresi, pt_ogretmenzilsuresi, pt_derssuresi)
                            self.kontrol['osderssaati'] = self.oglensonrasi(pt_oglenarasisuresi, cik)
                            print("{} : {}.Ders ilk {} , ders {} , çıkış {} ".format(self.gunler[gun_id], z, ilk, ders, cik))

                        if z > pt_oglenarasiders:
                            ilk, ders, cik = self.gunun_zili(z - pt_oglenarasiders, gun_id, self.kontrol.get('osderssaati'), pt_toplanmasuresi,
                                                             pt_tenefussuresi, pt_ogretmenzilsuresi, pt_derssuresi)
                            print("{} : {}.Ders ilk {} , ders {} , çıkış {} ".format(self.gunler[gun_id], z, ilk, ders,
                                                                                     cik))

                    if x.zilgun == 0:
                        for u in self.defaultgunhi():
                            pt_dersbaslangicsaati = x.dersbaslangicsaati
                            pt_toplanmasuresi = x.toplanmasuresi
                            pt_ogretmenzilsuresi = x.ogretmenzilsuresi
                            pt_derssayisi = x.derssayisi
                            pt_derssuresi = x.derssuresi
                            pt_tenefussuresi = x.tenefussuresi
                            pt_oglenarasiders = x.oglenarasiders
                            pt_oglenarasisuresi = x.oglenarasisuresi
                            gun_id = u
                            self.kontrol['toplangun'] = True
                            if pt_oglenarasiders == 0 or pt_oglenarasiders is None:
                                pt_oglenarasiders = pt_derssayisi

                            for z in range(1, pt_derssayisi + 1):
                                if z > 1:
                                    self.kontrol['toplangun'] = False
                                if z <= pt_oglenarasiders:
                                    ilk, ders, cik = self.gunun_zili(z, gun_id, pt_dersbaslangicsaati, pt_toplanmasuresi,
                                                                     pt_tenefussuresi, pt_ogretmenzilsuresi, pt_derssuresi)
                                    self.kontrol['osderssaati'] = self.oglensonrasi(pt_oglenarasisuresi, cik)
                                    print("{} : {}.Ders ilk {} , ders {} , çıkış {} ".format(self.gunler[gun_id], z, ilk, ders,
                                                                                             cik))

                                if z > pt_oglenarasiders:
                                    ilk, ders, cik = self.gunun_zili(z - pt_oglenarasiders, gun_id, self.kontrol.get('osderssaati'),
                                                                     pt_toplanmasuresi,
                                                                     pt_tenefussuresi, pt_ogretmenzilsuresi, pt_derssuresi)

                                    print("{} : {}.Ders ilk {} , ders {} , çıkış {} ".format(self.gunler[gun_id], z, ilk, ders,
                                                                                             cik))

                if x.zilgun in [5, 6]:
                    pt_dersbaslangicsaati = x.dersbaslangicsaati
                    pt_toplanmasuresi = x.toplanmasuresi
                    pt_ogretmenzilsuresi = x.ogretmenzilsuresi
                    pt_derssayisi = x.derssayisi
                    pt_derssuresi = x.derssuresi
                    pt_tenefussuresi = x.tenefussuresi
                    pt_oglenarasiders = x.oglenarasiders
                    pt_oglenarasisuresi = x.oglenarasisuresi
                    gun_id = x.zilgun
                    self.kontrol['toplangun'] = True
                    if pt_oglenarasiders == 0 or pt_oglenarasiders is None:
                        pt_oglenarasiders = pt_derssayisi

                    for z in range(1, pt_derssayisi + 1):
                        if z > 1:
                            self.kontrol['toplangun'] = False
                        if z <= pt_oglenarasiders:
                            ilk, ders, cik = self.gunun_zili(z, gun_id, pt_dersbaslangicsaati, pt_toplanmasuresi,
                                                             pt_tenefussuresi, pt_ogretmenzilsuresi, pt_derssuresi)
                            self.kontrol['osderssaati'] = self.oglensonrasi(pt_oglenarasisuresi, cik)
                            print("{} : {}.Ders ilk {} , ders {} , çıkış {} ".format(self.gunler[gun_id], z, ilk, ders, cik))
                        if z > pt_oglenarasiders:
                            ilk, ders, cik = self.gunun_zili(z - pt_oglenarasiders, gun_id, self.kontrol.get('osderssaati'),
                                                             pt_toplanmasuresi,
                                                             pt_tenefussuresi, pt_ogretmenzilsuresi, pt_derssuresi)

                            print("{} : {}.Ders ilk {} , ders {} , çıkış {} ".format(self.gunler[gun_id], z, ilk, ders,
                                                                                     cik))

            else:
                pass

        for u in self.defaultgunhi():
            print(f"Tanımlanmamış gün {self.gunler[u]} ..")


xd = ZilUret(ZilData, DersZamanlama)
xd.uret()

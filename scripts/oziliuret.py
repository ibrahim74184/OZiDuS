"""import os, sys
from pathlib import Path


if os.name=="posix":
    BASE_DIR = Path(__file__).resolve().parent.parent
elif os.name=="nt":
    BASE_DIR = Path(__file__).resolve().parent.parent
    BASE_DIR = str(BASE_DIR)[2:].replace("\\", '/')
else: print("Bulunamdı")

# Build paths inside the project like this: BASE_DIR / 'subdir'.


# This is so Django knows where to find stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ozidusproject.settings")
sys.path.append(BASE_DIR)

# This is so my local_settings.py gets loaded.
os.chdir(BASE_DIR)

# This is so models get loaded.
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()"""

from ozilanons.models import ZilData
from ozilanons.models import DersZamanlama
from datetime import datetime, time, timedelta

def gunun_zili(z, gun_id, pt_dersbaslangicsaati, pt_toplanmasuresi, pt_tenefussuresi, pt_ogretmenzilsuresi,
               pt_derssuresi):
    global toplangun
    if gun_id == 0 and toplangun:
        toplangun = False
        toplan_sa = int(pt_dersbaslangicsaati.hour)
        toplan_dk = int(pt_dersbaslangicsaati.minute) - pt_toplanmasuresi.minute
        if toplan_dk < 0:
            toplan_dk += 60
            toplan_sa -= 1
        toplan = "Toplanma {}:{}:00".format(toplan_sa, toplan_dk)
    else:
        toplan = None

    ilk, ders, cik = derszilihesapla(z, pt_dersbaslangicsaati, pt_derssuresi, pt_tenefussuresi, pt_ogretmenzilsuresi)
    return toplan, z, ilk, ders, cik


def derszilihesapla(z, dersbaslangicsaati='09:00:00',
                    derssuresi='00:30:00',
                    tenefussuresi='00:10:00',
                    ogretmenzilsuresi='00:03:00'):
    ss = int(dersbaslangicsaati.hour)
    ss_ders = int(dersbaslangicsaati.hour)
    ss_cik = int(dersbaslangicsaati.hour)
    ilk = ((dersbaslangicsaati.minute + (z - 1) * (
            derssuresi.minute + tenefussuresi.minute)) - ogretmenzilsuresi.minute)
    ders = (dersbaslangicsaati.minute + (z - 1) * (
            derssuresi.minute + tenefussuresi.minute))
    cik = dersbaslangicsaati.minute + z * derssuresi.minute + \
          (z - 1) * tenefussuresi.minute
    if ilk < 0:
        ilk += 60
        ss = ss - 1

    ss += int(ilk) // 60
    ss_ders += int(ders) // 60
    ss_cik += int(cik) // 60

    ilk %= 60
    ders %= 60
    cik %= 60
    return time(ss, ilk, 0), time(ss_ders, ders, 0), time(ss_cik, cik, 0)


def defaultgun():
    gziller = ZilData.objects.all()
    gundefault = list()
    for x in gziller:
        if x.active:
            if (x.zilgun in [0, 1, 2, 3, 4]) and (x.zilgun not in [5, 6]):
                gundefault.append(x.zilgun)

    xy = set(gundefault).symmetric_difference(set([0, 1, 2, 3, 4]))
    return xy


def uret():
    gziller = ZilData.objects.all()
    gunler = ['Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma', 'Cumartesi', 'Pazar']
    gundefault = list()

    all_fields = [f.name for f in DersZamanlama._meta.fields]
    # print(all_fields)
    global toplangun
    global toplan
    toplangun = True
    guncount = 0
    global element

    for x in gziller:
        if x.active:
            if (x.zilgun in [0, 1, 2, 3, 4]) and (x.zilgun not in [5, 6]):
                guncount += 1
                pt_toplanmasuresi = x.toplanmasuresi
                pt_dersbaslangicsaati = x.dersbaslangicsaati
                pt_ogretmenzilsuresi = x.ogretmenzilsuresi
                pt_derssayisi = x.derssayisi
                pt_derssuresi = x.derssuresi
                pt_tenefussuresi = x.tenefussuresi
                pt_oglenarasiders = x.oglenarasiders
                pt_oglenarasisuresi = x.oglenarasisuresi
                gundefault.append(x.zilgun)
                gun_id = x.zilgun

                for z in range(1, pt_oglenarasiders + 1):
                    toplan, z, ilk, ders, cik = gunun_zili(z, gun_id, pt_dersbaslangicsaati, pt_toplanmasuresi,
                                                           pt_tenefussuresi, pt_ogretmenzilsuresi, pt_derssuresi)

                    if toplan is not None:
                        print(toplan)
                    print("{} : {}.Ders ilk {} , ders {} , çıkış {} ".format(gunler[gun_id], z, ilk, ders, cik))
                    if z == pt_oglenarasiders:
                        oss = pt_oglenarasisuresi.hour
                        odd = pt_oglenarasisuresi.minute
                        ss = cik.hour
                        dd = cik.minute
                        ss += ((dd + odd) // 60)
                        ss += oss
                        dd = (odd + dd) % 60
                        element = time(ss, dd, 0)

                for z in range(pt_oglenarasiders + 1, pt_derssayisi + 1):
                    toplan, u, ilk, ders, cik = gunun_zili(z - pt_oglenarasiders, gun_id, element, pt_toplanmasuresi,
                                                           pt_tenefussuresi, pt_ogretmenzilsuresi, pt_derssuresi)

                    if toplan is not None:
                        print(toplan)
                    print("{} : {}.Ders ilk {} , ders {} , çıkış {} ".format(gunler[gun_id], z, ilk, ders, cik))

                """---------------------------------------------"""
                if x.zilgun == 0:
                    for u in defaultgun():

                        guncount += 1
                        pt_dersbaslangicsaati = x.dersbaslangicsaati
                        pt_toplanmasuresi = x.toplanmasuresi
                        pt_ogretmenzilsuresi = x.ogretmenzilsuresi
                        pt_derssayisi = x.derssayisi
                        pt_derssuresi = x.derssuresi
                        pt_tenefussuresi = x.tenefussuresi
                        pt_oglenarasiders = x.oglenarasiders
                        pt_oglenarasisuresi = x.oglenarasisuresi
                        gun_id = u

                        for z in range(1, pt_oglenarasiders + 1):
                            toplan, z, ilk, ders, cik = gunun_zili(z, gun_id, pt_dersbaslangicsaati, pt_toplanmasuresi,
                                                                   pt_tenefussuresi, pt_ogretmenzilsuresi,
                                                                   pt_derssuresi)

                            if toplan is not None:
                                print(toplan)
                            print("{} : {}.Ders ilk {} , ders {} , çıkış {} ".format(gunler[gun_id], z, ilk, ders, cik))
                            if z == pt_oglenarasiders:
                                oss = pt_oglenarasisuresi.hour
                                odd = pt_oglenarasisuresi.minute
                                ss = cik.hour
                                dd = cik.minute
                                ss += ((dd + odd) // 60)
                                ss += oss
                                dd = (odd + dd) % 60
                                element = time(ss, dd, 0)

                        for z in range(pt_oglenarasiders + 1, pt_derssayisi + 1):
                            toplan, u, ilk, ders, cik = gunun_zili(z - pt_oglenarasiders, gun_id, element,
                                                                   pt_toplanmasuresi,
                                                                   pt_tenefussuresi, pt_ogretmenzilsuresi,
                                                                   pt_derssuresi)

                            if toplan is not None:
                                print(toplan)
                            print("{} : {}.Ders ilk {} , ders {} , çıkış {} ".format(gunler[gun_id], z, ilk, ders, cik))
                """---------------------------------------------"""

            if x.zilgun in [5, 6]:
                guncount += 1
                pt_dersbaslangicsaati = x.dersbaslangicsaati
                pt_toplanmasuresi = x.toplanmasuresi
                pt_ogretmenzilsuresi = x.ogretmenzilsuresi
                pt_derssayisi = x.derssayisi
                pt_derssuresi = x.derssuresi
                pt_tenefussuresi = x.tenefussuresi
                pt_oglenarasiders = x.oglenarasiders
                pt_oglenarasisuresi = x.oglenarasisuresi
                gun_id = x.zilgun

                for z in range(1, pt_oglenarasiders + 1):
                    toplan, z, ilk, ders, cik = gunun_zili(z, gun_id, pt_dersbaslangicsaati, pt_toplanmasuresi,
                                                           pt_tenefussuresi, pt_ogretmenzilsuresi, pt_derssuresi)

                    if toplan is not None:
                        print(toplan)
                    print("{} : {}.Ders ilk {} , ders {} , çıkış {} ".format(gunler[gun_id], z, ilk, ders, cik))
                    if z == pt_oglenarasiders:
                        oss = pt_oglenarasisuresi.hour
                        odd = pt_oglenarasisuresi.minute
                        ss = cik.hour
                        dd = cik.minute
                        ss += ((dd + odd) // 60)
                        ss += oss
                        dd = (odd + dd) % 60
                        element = time(ss, dd, 0)

                for z in range(pt_oglenarasiders + 1, pt_derssayisi + 1):
                    toplan, u, ilk, ders, cik = gunun_zili(z - pt_oglenarasiders, gun_id, element, pt_toplanmasuresi,
                                                           pt_tenefussuresi, pt_ogretmenzilsuresi, pt_derssuresi)

                    if toplan is not None:
                        print(toplan)
                    print("{} : {}.Ders ilk {} , ders {} , çıkış {} ".format(gunler[gun_id], z, ilk, ders, cik))

        else:
            pass

    """# xy = set(gundefault).symmetric_difference(set([0, 1, 2, 3, 4]))
    for x in gziller:
        if x.active:
            if x.zilgun == 0:
                for u in defaultgun():

                    guncount += 1
                    pt_dersbaslangicsaati = x.dersbaslangicsaati
                    pt_toplanmasuresi = x.toplanmasuresi
                    pt_ogretmenzilsuresi = x.ogretmenzilsuresi
                    pt_derssayisi = x.derssayisi
                    pt_derssuresi = x.derssuresi
                    pt_tenefussuresi = x.tenefussuresi
                    pt_oglenarasiders = x.oglenarasiders
                    pt_oglenarasisuresi = x.oglenarasisuresi
                    gun_id = u

                    for z in range(1, pt_oglenarasiders + 1):
                        toplan, z, ilk, ders, cik = gunun_zili(z, gun_id, pt_dersbaslangicsaati, pt_toplanmasuresi,
                                                               pt_tenefussuresi, pt_ogretmenzilsuresi, pt_derssuresi)

                        if toplan is not None:
                            print(toplan)
                        print("{} : {}.Ders ilk {} , ders {} , çıkış {} ".format(gunler[gun_id], z, ilk, ders, cik))
                        if z == pt_oglenarasiders:
                            oss = pt_oglenarasisuresi.hour
                            odd = pt_oglenarasisuresi.minute
                            ss = cik.hour
                            dd = cik.minute
                            ss += ((dd + odd) // 60)
                            ss += oss
                            dd = (odd + dd) % 60
                            element = time(ss, dd, 0)

                    for z in range(pt_oglenarasiders + 1, pt_derssayisi + 1):
                        toplan, u, ilk, ders, cik = gunun_zili(z - pt_oglenarasiders, gun_id, element,
                                                               pt_toplanmasuresi,
                                                               pt_tenefussuresi, pt_ogretmenzilsuresi, pt_derssuresi)

                        if toplan is not None:
                            print(toplan)
                        print("{} : {}.Ders ilk {} , ders {} , çıkış {} ".format(gunler[gun_id], z, ilk, ders, cik))"""
    for u in defaultgun():
        print(f"Tanımlanmamış gün {gunler[u]} ..")

df = defaultgun()
uret()

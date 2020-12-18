import os, sys

proj_path = "/Users/Samsung/Desktop/PythonProjeler/OZiDuS"
# This is so Django knows where to find stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ozidusproject.settings")
sys.path.append(proj_path)

# This is so my local_settings.py gets loaded.
os.chdir(proj_path)

# This is so models get loaded.
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

from ozilanons.models import ZilData
from ozilanons.models import DersZamanlama
from datetime import datetime, timedelta
from math import fmod


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
        toplan = "Toplanma {}:{}".format(toplan_sa, toplan_dk)
    else:
        toplan = None

    ss = int(pt_dersbaslangicsaati.hour)
    ss_ders = int(pt_dersbaslangicsaati.hour)
    ss_cik = int(pt_dersbaslangicsaati.hour)
    ilk = ((pt_dersbaslangicsaati.minute + (z - 1) * (
            pt_derssuresi.minute + pt_tenefussuresi.minute)) - pt_ogretmenzilsuresi.minute)
    ders = (pt_dersbaslangicsaati.minute + (z - 1) * (
            pt_derssuresi.minute + pt_tenefussuresi.minute))
    cik = pt_dersbaslangicsaati.minute + z * pt_derssuresi.minute + \
          (z - 1) * pt_tenefussuresi.minute
    if ilk < 0:
        ilk += 60
        ss = ss - 1

    ss += int(ilk) // 60
    ss_ders += int(ders) // 60
    ss_cik += int(cik) // 60

    ilk %= 60
    ders %= 60
    cik %= 60
    return z, ss, ilk, ss_ders, ders, ss_cik, cik, toplan


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

                for z in range(1, pt_oglenarasiders + 1):
                    gun_id = x.zilgun
                    z, ss, ilk, ss_ders, ders, ss_cik, cik, toplan = gunun_zili(z, gun_id,
                                                                                pt_dersbaslangicsaati,
                                                                                pt_toplanmasuresi, pt_tenefussuresi,
                                                                                pt_ogretmenzilsuresi, pt_derssuresi)

                    if toplan is not None:
                        print(toplan)
                    print("{} : {}.Ders ilk {}:{} , ders {}:{} , çıkış {}:{} ".format(gunler[gun_id], z, ss, ilk,
                                                                                  ss_ders, ders, ss_cik, cik))

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
                for z in range(1, pt_oglenarasiders + 1):
                    gun_id = x.zilgun
                    z, ss, ilk, ss_ders, ders, ss_cik, cik, toplan = gunun_zili(z, gun_id,
                                                                                pt_dersbaslangicsaati,
                                                                                pt_toplanmasuresi, pt_tenefussuresi,
                                                                                pt_ogretmenzilsuresi, pt_derssuresi)

                    if toplan is not None:
                        print(toplan)
                    print("{} : {}.Ders ilk {}:{} , ders {}:{} , çıkış {}:{} ".format(gunler[gun_id], z, ss, ilk,
                                                                                      ss_ders, ders, ss_cik, cik))

        else:
            pass

    xy = set(gundefault).symmetric_difference(set([0, 1, 2, 3, 4]))
    for x in gziller:
        if x.active:
            if x.zilgun == 0:
                for u in xy:

                    guncount += 1
                    pt_dersbaslangicsaati = x.dersbaslangicsaati
                    pt_toplanmasuresi = x.toplanmasuresi
                    pt_ogretmenzilsuresi = x.ogretmenzilsuresi
                    pt_derssayisi = x.derssayisi
                    pt_derssuresi = x.derssuresi
                    pt_tenefussuresi = x.tenefussuresi
                    pt_oglenarasiders = x.oglenarasiders
                    pt_oglenarasisuresi = x.oglenarasisuresi
                    for z in range(1, pt_oglenarasiders + 1):
                        gun_id = u
                        z, ss, ilk, ss_ders, ders, ss_cik, cik, toplan = gunun_zili(z, gun_id,
                                                                                    pt_dersbaslangicsaati,
                                                                                    pt_toplanmasuresi, pt_tenefussuresi,
                                                                                    pt_ogretmenzilsuresi, pt_derssuresi)

                        if toplan is not None:
                            print(toplan)
                        print("{} : {}.Ders ilk {}:{} , ders {}:{} , çıkış {}:{} ".format(gunler[gun_id], z, ss, ilk,
                                                                                          ss_ders, ders, ss_cik, cik))
    for u in xy:
        print(f"Tanımlanmamış gün {gunler[u]} ..")


uret()

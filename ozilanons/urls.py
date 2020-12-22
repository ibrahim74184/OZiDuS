from django.urls import path
from ozilanons.views import login_zil, AksamZilDataListView, guncelle, cikis, icerikSil, new_post_zildata, ZilListView
from ozilanons.views import ZilDataListView, index, post_zildata_new, post_aksamzildata_new, zilayarmenu
from ozilanons.views import ZilListViewAksam, duyurumetin, zilikapat, anonsduyuru

urlpatterns = [
    path('', login_zil, name='login'),
    path('home/cikis', cikis, name='cikis'),
    path('home/', index, name='index'),
    path('home/okul/edit/<int:id>', guncelle, name='guncelle'),
    path('home/okul/sil/<int:id>', icerikSil, name='sil'),
    path('home/okul/duyurumetin/', duyurumetin, name='duyurumetin'),
    path('home/okul/anonsduyuru/', anonsduyuru, name='anonsduyuru'),
    path('home/okul/zilikapat/', zilikapat, name='zilikapat'),
    path('home/okul/', zilayarmenu, name='zilayarmenu'),
    path('home/okul/odata/', ZilListView, name='zillistview'),
    path('home/okul/oadata/', ZilListViewAksam, name='zillistviewaksam'),
    path('home/okul/new2/', new_post_zildata, name='new2'),
    path('home/okul/new/', post_zildata_new, name='okul_new'),
    path('home/okul/aksam/new/', post_aksamzildata_new, name='aksam_new'),

]

# path('home/okul/ozilaksamdata/', AksamZilDataListView.as_view(), name='ozilaksamdata'),
# path('home/okul/ozildata/', ZilDataListView.as_view(), name='ozildata'),
# path('home/okul/anonsduyuru/', anonsduyuru, name='anonsduyuru'),

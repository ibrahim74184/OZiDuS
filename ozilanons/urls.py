from django.urls import path
from ozilanons.views import login_zil, AksamZilDataListView, guncelle, cikis
from ozilanons.views import ZilDataListView, index, post_zildata_new, post_aksamzildata_new, zilayarmenu, anonsduyuru

urlpatterns = [
    path('', login_zil, name='login'),
    path('home/cikis', cikis, name='cikis'),
    path('home/', index, name='index'),
    path('home/<int:id>', guncelle, name='guncelle'),
    path('home/okul/', zilayarmenu, name='zilayarmenu'),
    path('home/okul/anonsduyuru/', anonsduyuru, name='anonsduyuru'),
    path('home/okul/ozildata/', ZilDataListView.as_view(), name='ozildata'),
    path('home/okul/ozilaksamdata/', AksamZilDataListView.as_view(), name='ozilaksamdata'),
    path('home/okul/new/', post_zildata_new, name='okul_new'),
    path('home/okul/aksam/new/', post_aksamzildata_new, name='aksam_new'),

]

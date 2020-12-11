from django.urls import path
from ozilanons.views import ZilDataListView, index, post_zildata_new, post_zildata_detail, post_anons_new


urlpatterns = [
    path('', index, name='index'),
    path('ozildata/', ZilDataListView.as_view(), name='ozildata'),
    path('ozildata/<int:pk>/', post_zildata_detail, name='post_detail'),
    path('new/', post_zildata_new, name='post_new'),
    path('newduyuru/', post_anons_new, name='post_new_duyuru'),

]

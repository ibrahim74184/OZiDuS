from django.urls import path
from ozilanons.views import ZilDataListView, index, post_zildata_new, post_zildata_detail


urlpatterns = [
    path('', index, name='index'),
    path('ozildata/', ZilDataListView.as_view(), name='zilayarlari'),
    path('ozildata/<int:pk>/', post_zildata_detail, name='post_detail'),
    path('new/', post_zildata_new, name='post_new'),

]

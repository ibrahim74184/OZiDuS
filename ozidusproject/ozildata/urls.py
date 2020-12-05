from django.urls import path
from ozildata.views import ZilDataListView, index, post_new, post_detail


urlpatterns = [
    path('', index, name='index'),
    path('ozildata/', ZilDataListView.as_view(), name='zilayarlari'),
    path('ozildata/<int:pk>/', post_detail, name='post_detail'),
    path('new/', post_new, name='post_new'),

]

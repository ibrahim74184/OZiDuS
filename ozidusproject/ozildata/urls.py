from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='ozildata'),
    path('ozildata/<int:pk>/', views.post_detail, name='post_detail'),
    path('new/', views.post_new, name='post_new'),
]

# path('detail/', views.detail, name ='detail'),
# path('', views.post_list, name='post_list'),
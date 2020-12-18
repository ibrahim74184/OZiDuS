from django.contrib import admin
from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('kayit',views.kayit,name='kayit'),
    path('giris',views.giris, name="giris"),
    path('cikis',views.cikis, name="cikis"),
    path('kontrolpanel',views.kontrolpanel, name="kontrolpanel"),
]
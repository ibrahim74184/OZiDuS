from django.urls import path
from home.views import home_views

urlpatterns = [
    path('', home_views, name='home'),

]
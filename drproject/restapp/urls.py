from django.urls import path
from restapp.views import home

urlpatterns = [
    path('', home, name='home'),
]
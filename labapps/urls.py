from django.urls import path
from labapps import views

urlpatterns = [
    path('molemule', views.molemule, name='molemule'),
    path('nucleo', views.nucleo, name='nucleo'),
    path('pyteins', views.pyteins, name='pyteins'),
]

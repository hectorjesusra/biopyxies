from django.urls import path, include
from home import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('lab/', include('lab.urls')),
    path('contact', views.contact, name='contact'),
    path('forum/', include('forum.urls')),
]

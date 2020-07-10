from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('lab', views.lab, name='lab'),
    path('contact', views.contact, name='contact'),
    path('forum', views.forum, name='forum'),
]

from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('lab', views.lab, name='lab'),
    path('lab/about', views.lababout, name='lababout'),
    path('lab/apps', views.labapps, name='labapps'),
    path('lab/apps/molemule', views.molemule, name='molemule'),
    path('lab/apps/nucleo', views.nucleo, name='nucleo'),
    path('lab/apps/pyteins', views.pyteins, name='pyteins'),
    path('lab/tutorial', views.labtutorial, name='labtutorial'),
    path('contact', views.contact, name='contact'),
    path('forum', views.forum, name='forum'),
]

from django.urls import path, include
from forum import views


urlpatterns = [
    path('login/', views.loginpage, name='login'),
    path('register/', views.registerpage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/',views.profile, name='profile'),
    path('', views.forum, name='forum'),
]

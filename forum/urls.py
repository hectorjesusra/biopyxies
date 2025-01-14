from django.urls import path, include
from forum import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path('login/', views.loginpage, name='login'),
    path('register/', views.registerpage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/',views.profile, name='profile'),
    path('', PostListView.as_view(), name='forum'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(),name='post-delete'),
]

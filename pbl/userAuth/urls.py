from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.entry, name="entry"),
    path('home/', views.home, name="home"),
    path('menu/', views.menu, name="menu"),
    path('register/', views.userRegister, name="register"),
    path('login/', views.userLogin, name="login"),
    path('logout/', views.userLogout, name="logout"),
    path('logout/', views.NA, name="NA"),
]
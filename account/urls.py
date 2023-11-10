from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_info),
    path('login/', views.login, name='login'),
    path('user_info/', views.user_info, name='user_info'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]
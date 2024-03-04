from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('settings/', views.settings, name='settings'),
    path('search-armstrong/', views.search_armstrong, name='search_armstrong'),
    path('check-armstrong/', views.check_armstrong, name='check_armstrong'),
]

from django.urls import path
from .import views

urlpatterns = [
    path('',views.loginPage, name='login'),

    path('register/', views.userRegistration, name='register'),

    path('logout/', views.logoutView, name='logout')
    
]
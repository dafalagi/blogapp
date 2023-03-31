from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # This is the path to the components page
    path('components/<str:title>', views.components, name='components'),

    # This is the path to the forms page
    path('forms/<str:title>', views.forms, name='forms'),

    # This is the path to the tables page
    path('data-tables/', views.data_tables, name='data-tables'),

    # This is the path to the icons page
    path('icons/<str:title>', views.icons, name='icons'),

    # This is the path to the profile page
    path('profile/', views.profile, name='profile'),

    # This is the path to the faq page
    path('faq/', views.faq, name='faq'),

    # This is the path to the contact page
    path('contact/', views.contact, name='contact'),

    # This is the path to the register page
    path('register/', views.register, name='register'),

    # This is the path to the login page
    path('login/', views.login, name='login'),

    # This is the path to the error page
    path('error/', views.error, name='error'),

    # This is the path to the blank page
    path('blank/', views.blank, name='blank'),

]
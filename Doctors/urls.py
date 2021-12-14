from django.contrib import admin
from django.urls import path
from Doctors import views as doctor_view

app_name = 'Doctors'

urlpatterns = [
    path('signup/', doctor_view.signup, name='signup'),
    path('login/', doctor_view.login, name='login'),
    path('<name>/dashboard/', doctor_view.dashboard, name='dashboard'),
    path('logout/', doctor_view.logout, name='logout'),
]
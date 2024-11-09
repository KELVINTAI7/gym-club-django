from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('classes', views.classes, name='classes'),
    path('trainers', views.trainers, name='trainers'),
    path('contact', views.contact, name='contact'),

]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница приложения 'schedule'
    path('budva-sveti-stefan-budva.html', views.sveti_stefan, name='sveti_stefan'),
    path('budva-petrovac-budva.html', views.petrovac, name='petrovac'),
    path('budva-lastva-budva.html', views.lastva, name='lastva'),
]

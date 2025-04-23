from django.urls import path
from . import views

urlpatterns = [
    path('fact/', views.fact, name='fact'),
    path('home/', views.home, name='home'),
    path('', views.home),
]

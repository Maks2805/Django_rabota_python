from django import views
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index),
    path('name/', views.name),
    path('Tom/', views.tom)
]

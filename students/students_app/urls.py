from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_student/', views.add_student, name='add-student'),
    path('', views.search_form, name="search-form"),
    path('search/', views.search, name="search"),
]

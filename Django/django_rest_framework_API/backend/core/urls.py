from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.ContactAPIView.as_view(), name="index"),
    path('get_contact/', views.get, name="index"),
    path('update_contact/', views.get, name="index"),
    path('delete_contact/', views.get, name="index"),
]
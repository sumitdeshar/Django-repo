from django.contrib import admin
from django.urls import path
from ecommerce import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'item', views.ItemViewSet, basename='item')
router.register(r'order', views.OrderViewSet, basename='order')

urlpatterns = router.urls

urlpatterns = [
    #path('',views.index,name='index'),
]


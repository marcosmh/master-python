from django.urls import path
from . import views

urlpatterns = [
    path('categoria/', views.category, name="categoria"),
    path('articulos/', views.list, name="articulos"),
]
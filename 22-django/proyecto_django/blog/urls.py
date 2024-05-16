from django.urls import path
from . import views

urlpatterns = [
    path('categoria/', views.category, name="categoria"),
    path('articulo/', views.article, name="articulo"),
]
from django.urls import path
from . import views

urlpatterns = [
    path('category/<int:category_id>', views.category, name="category"),
    path('articulos/', views.list, name="articulos"),
    path('articulo/<int:article_id>', views.article, name="article"),
]
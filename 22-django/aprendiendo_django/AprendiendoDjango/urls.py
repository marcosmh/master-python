"""AprendiendoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings

# Importar app con mis vistas
from miapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('inicio/', views.index, name="inicio"),
    path('hola-mundo/',views.hola_mundo, name="hola_mundo"),
    path('pagina/',views.pagina, name="pagina"),
    path('pagina/<int:rediregir>',views.pagina, name="pagina"),
    path('contacto/',views.contacto, name="contacto"),
    path('contacto/<str:nombre>/',views.contacto, name="contacto"),
    path('contacto/<str:nombre>/<str:apellidos>',views.contacto, name="contacto"),
    path('crear-articulo/<str:title>/<str:content>/<str:public>',views.crear_articulo, name="crear_articulo"),
    path('articulo/',views.articulo, name="articulo"),
    path('articulos/',views.articulos, name="articulos"),
    path('actualizar_articulo/<int:id>',views.actualizar_articulo, name="actualizar_articulo"),
    path('borrar_articulo/<int:id>',views.borrar_articulo, name="borrar_articulo"),
    path('save_article/',views.save_article, name="save_article"),
    path('create_article/',views.create_article, name="create_article"),
    path('create_full_article/',views.create_full_article, name="create_full_article"),
]


#configuaración para cargar imágenes
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
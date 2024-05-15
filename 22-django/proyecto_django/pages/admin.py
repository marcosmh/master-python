from django.contrib import admin
from .models import Page

# Register your models here.
admin.site.register(Page)

#configuar panel
title = "Panel Control de Páginas"
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = "Panel de Control"
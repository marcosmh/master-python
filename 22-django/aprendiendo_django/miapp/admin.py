from django.contrib import admin
from .models import Article, Category

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','update_at')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)

#configuar el titulo del panel
title = "Master en Pythonx"
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = "Panel de Gestión"
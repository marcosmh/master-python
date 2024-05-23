from django.contrib import admin
from .models import Category, Article

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','update_at')
    list_display = ('name','created_at')
    search_fields = ('name','description')

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('user','created_at','update_at')
    search_fields = ('title','content','user__name','categories__name')
    list_display = ('title','user','public','created_at')
    list_filter = ('public','user','categories__name')

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id

        obj.save()


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)

#configuar panel
title = "Panel Control de Blog"
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = "Panel de Control"

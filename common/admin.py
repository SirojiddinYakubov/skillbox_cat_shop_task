from django.contrib import admin

from common.models import Cat


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']

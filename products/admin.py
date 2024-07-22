from django.contrib import admin
from .models import Categories,Products
from import_export.admin import ImportExportModelAdmin

# admin.site.register(Products)

@admin.register(Categories)
class CategoriesAdmin(ImportExportModelAdmin):
    list_display = ('title','slug','image','description','count')
    ordering = ('title',)

@admin.register(Products)
class ProductsAdmin(ImportExportModelAdmin):
    list_display =('title','slug','descriptions','image','price','count')
    ordering = ('title',)



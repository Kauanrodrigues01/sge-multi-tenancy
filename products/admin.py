from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'brand', 'description')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'updated_at')
    
admin.site.register(Product, ProductAdmin)
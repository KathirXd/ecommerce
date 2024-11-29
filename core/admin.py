# admin.py
from django.contrib import admin
from .models import Product, Cart,CartItem
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
admin.site.register(Cart)
admin.site.register(CartItem)
if not admin.site.is_registered(Product):
    admin.site.register(Product)



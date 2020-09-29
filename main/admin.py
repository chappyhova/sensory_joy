from django.contrib import admin
from .models import Product, Basket, BasketItem, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'long_description', 'price', 'image')

admin.site.register(Product, ProductAdmin)
admin.site.register(Basket)
admin.site.register(BasketItem)
admin.site.register(Category)

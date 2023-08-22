from django.contrib import admin
from .models import Product, CardProduct, Cart, Category, Order, Album

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","title")
    prepopulated_fields = {"slug":("title",)}

admin.site.register(Product)
admin.site.register(CardProduct)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Album)
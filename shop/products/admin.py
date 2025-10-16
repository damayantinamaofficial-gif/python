from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','category','price','created_at')
    list_filter = ('name','category')
    search_field = ('name','description')


admin.site.register(Product,ProductAdmin)
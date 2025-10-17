from django.contrib import admin
from .models import Product,Category

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','category','price','created_at')
    list_filter = ('name','category')
    search_field = ('name','description')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')

admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
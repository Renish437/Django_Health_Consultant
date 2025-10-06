from django.contrib import admin

# Register your models here.
from .models import *
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':("category_name",)}
    list_display = ('id','category_name','slug')
    
admin.site.register(Category,CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':("product_name",)}
    list_display = ('id','product_name','price','category','stock','is_available')
    
admin.site.register(Product,ProductAdmin)
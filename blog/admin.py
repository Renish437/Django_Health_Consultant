from django.contrib import admin
from .models import *
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('category_name',)}
    
admin.site.register(Category,CategoryAdmin)


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
    
admin.site.register(Blog,BlogAdmin)
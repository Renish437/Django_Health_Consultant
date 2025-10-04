from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=100,unique=True)
    description = models.TextField(blank=True)
    cat_image = models.ImageField(upload_to='shop/categories',blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'shop_category'
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.category_name



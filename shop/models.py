from django.db import models

# Create your models here.
from django.urls import reverse

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


class Product(models.Model):
    product_name = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='shop/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    rating = models.IntegerField(null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="product_category")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_detail_url(self):
        return reverse('product-detail',args={self.category.slug,self.slug})
    
    class Meta:
        db_table = 'shop_products'
        managed = True
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        
    def __str__(self):
        return self.product_name
        
    



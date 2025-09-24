from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural ="Categories"
    def __str__(self):
        return self.category_name

STATUS_CHOICES = (
    ('Draft','Draft'),
    ('Published','Published')
)
class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug= models.SlugField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='blog_category')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/blogs/')
    short_description = models.TextField(max_length=1000)
    description = models.TextField()
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='Draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural ="Blogs"
    def __str__(self):
        return self.title
    
    

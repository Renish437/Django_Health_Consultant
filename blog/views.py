from django.shortcuts import render,get_object_or_404
from .models import *
# Create your views here.

def blogs(request):
    
    blogs = Blog.objects.filter(status='Published')
    context = {
      
        'blogs':blogs
    }
    return render(request,'blogs/blogs.html',context)


def post_by_category(request,category_id):
    blogs = Blog.objects.filter(status="Published",category=category_id)
    category = get_object_or_404(Category,id=category_id)
    context = {
        'category':category,
        'blogs':blogs
    }
    return render(request,'blogs/posts_by_category.html',context)
    
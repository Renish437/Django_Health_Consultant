from django.shortcuts import render
from .models import *
# Create your views here.

def blogs(request):
    categories = Category.objects.all()
    blogs = Blog.objects.all()
    context = {
        'categories':categories,
        'blogs':blogs
    }
    return render(request,'blogs/blogs.html',context)
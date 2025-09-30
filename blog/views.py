from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from .models import *
# Create your views here.

def blogs(request):
    keyword = request.GET.get('keyword')
    if keyword:
        blogs=Blog.objects.filter(Q(title__icontains=keyword) | Q(category__category_name__icontains=keyword)| Q(short_description__icontains=keyword),status="Published")
    else:
        blogs = Blog.objects.filter(status='Published')
    
    paginator = Paginator(blogs,4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
      
        'blogs':blogs,
        'page_obj':page_obj
    }
    return render(request,'blogs/blogs.html',context)


def post_by_category(request,category_id):
    keyword = request.GET.get('keyword')
    if keyword:
        blogs=Blog.objects.filter(Q(title__icontains=keyword) | Q(category__category_name__icontains=keyword)| Q(short_description__icontains=keyword),status="Published",category=category_id)
    else:
        blogs = Blog.objects.filter(status="Published",category=category_id)
    
    category = get_object_or_404(Category,id=category_id)
    paginator = Paginator(blogs,4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'category':category,
        'blogs':blogs,
        'page_obj':page_obj
    }
    return render(request,'blogs/posts_by_category.html',context)


    
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


from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Blog, Category

def post_by_category(request, category_slug):
    # Get the category object first
    category = get_object_or_404(Category, slug=category_slug)

    # Get the search keyword if any
    keyword = request.GET.get('keyword')

    if keyword:
        # Filter blogs by keyword (title or short_description) AND category
        blogs = Blog.objects.filter(
            Q(title__icontains=keyword) |
            Q(short_description__icontains=keyword),
            status="Published",
            category=category
        )
    else:
        # Just get all published blogs for this category
        blogs = Blog.objects.filter(status="Published", category=category)

    # Pagination
    paginator = Paginator(blogs, 4)  # 4 blogs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Context
    context = {
        'category': category,
        'blogs': blogs,
        'page_obj': page_obj
    }

    return render(request, 'blogs/posts_by_category.html', context)



def singleBlog(request,slug):
    blog = get_object_or_404(Blog,slug=slug,status="Published")
    context={
        'blog':blog
    }
    return render(request,'blogs/single-blog.html',context)


    
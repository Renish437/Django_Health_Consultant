from django.shortcuts import render,get_object_or_404
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.

def shops(request):
    keyword = request.GET.get('keyword')
    if keyword:
        products = Product.objects.filter(
            Q(product_name__icontains=keyword) |
            Q(description__icontains=keyword),
            is_available=True,
        )
    else:
        products = Product.objects.filter(is_available=True, stock__gt=0).order_by('-created_at')
    
    paginator = Paginator(products, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj
    }
    return render(request, 'shops/shop.html', context)


def checkouts(request):
    return render(request,'checkouts/checkout.html')


def cart_view(request):
    return render(request,'shops/cart.html')

def product_category(request,slug):
    category = get_object_or_404(Category,slug=slug)
    
    keyword = request.GET.get('keyword')
    if keyword:
        products = Product.objects.filter(
            Q(product_name__icontains=keyword) |
            Q(description__icontains=keyword),
            is_available=True,
            category=category
        )
    else:
        products = Product.objects.filter(category=category,is_available=True)
    
    # Pagination
    paginator = Paginator(products, 4)  # 4 blogs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context={
        'category':category,
        
          'page_obj':page_obj
    }
    return render(request,'shops/shop-category.html',context)
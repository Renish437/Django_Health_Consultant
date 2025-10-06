from django.shortcuts import render
from .models import *
# Create your views here.

def shops(request):
    shop_categories = Category.objects.filter(is_active=True)
    products = Product.objects.filter(is_available=True,stock__gt=0).order_by('-created_at')
    context={
        "shop_categories":shop_categories,
        "products":products
    }
    return render(request,'shops/shop.html',context)

def checkouts(request):
    return render(request,'checkouts/checkout.html')


def cart_view(request):
    return render(request,'shops/cart.html')
from django.shortcuts import render
from .models import *
# Create your views here.

def shops(request):
    shop_categories = Category.objects.filter(is_active=True)
    context={
        "shop_categories":shop_categories
    }
    return render(request,'shops/shop.html',context)

def checkouts(request):
    return render(request,'checkouts/checkout.html')


def cart_view(request):
    return render(request,'shops/cart.html')
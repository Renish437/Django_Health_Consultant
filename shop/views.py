from django.shortcuts import render

# Create your views here.

def shops(request):
    return render(request,'shops/shop.html')

def checkouts(request):
    return render(request,'checkouts/checkout.html')
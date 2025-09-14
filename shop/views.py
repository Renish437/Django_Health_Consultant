from django.shortcuts import render

# Create your views here.

def shops(request):
    return render(request,'shops/index.html')

def checkouts(request):
    return render(request,'checkouts/index.html')
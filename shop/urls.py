from django.urls import path 
from . import views

urlpatterns = [
     path('',views.shops,name='shops'),
    path('cart/',views.cart_view,name="cart"),
    path('checkout/',views.checkouts,name="checkouts"),
]

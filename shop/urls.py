from django.urls import path 
from . import views

urlpatterns = [
     path('',views.shops,name='shops'),
    path('cart/',views.cart_view,name="cart"),
    path('checkout/',views.checkouts,name="checkouts"),
    path('product-category/<slug:slug>',views.product_category,name="product_category"),
    path('product-search/',views.shops,name="shop_search")
]

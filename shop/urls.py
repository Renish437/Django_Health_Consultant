from django.urls import path 
from . import views

urlpatterns = [
     path('',views.shops,name='shops'),
    path('cart/',views.cart_view,name="cart"),
    path('checkout/',views.checkouts,name="checkouts"),
    path('product-category/<slug:slug>',views.product_category,name="product_category"),
    path('product-detail/<slug:category_slug>/<slug:product_slug>',views.product_detail,name="product-detail"),
    path('product-search/',views.shops,name="shop_search"),
    path('shopping-cart/',views.shopping_cart,name="shopping-cart"),
    path('add-to-cart/<int:product_id>/',views.add_to_cart,name="add-to-cart")
    
]

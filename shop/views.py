from django.shortcuts import render,get_object_or_404,redirect
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
    
    paginator = Paginator(products, 6)
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
    paginator = Paginator(products, 6)  # 4 blogs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context={
        'category':category,
        
          'page_obj':page_obj
    }
    return render(request,'shops/shop-category.html',context)



def product_detail(request, category_slug=None, product_slug=None):
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
    context = {'product': product}
    return render(request, 'shops/product-detail.html', context)



def _cart_id(request):
    """Get or create a unique cart ID for the session."""
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def shopping_cart(request, total=0, quantity=0, cart_items=None):
    """Display the shopping cart page."""
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += cart_item.product.price * cart_item.quantity
            quantity += cart_item.quantity
    except Cart.DoesNotExist:
        cart_items = []

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
    }

    return render(request, 'shops/shopping-cart.html', context)


def add_to_cart(request, product_id):
    """Add a product to the cart or increase its quantity."""
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(cart_id=_cart_id(request))

    try:
        # If the item already exists in the cart, increase its quantity
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        # Otherwise, create a new cart item
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart
        )

    return redirect('shopping-cart')

            
from .models import *
from blog.models import *
from shop.models import Category as ShopCategory,Product

def top_navbar(request):
    
    topnav = TopNavbar.objects.first()
    return dict(topnav=topnav)


def about(request):
    about = About.objects.first()
    return {"about":about}

def services(request):
    services = Services.objects.all()
    return {"services":services}
def categories(request):
    categories = Category.objects.all()
    return {"categories":categories}

def product_categories(request):
    
    product_categories = ShopCategory.objects.filter(is_active=True)
    product_count = Product.objects.count()
    return {"product_categories":product_categories,'product_count':product_count}
    
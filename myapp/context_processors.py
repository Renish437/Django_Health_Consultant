from .models import *

def top_navbar(request):
    
    topnav = TopNavbar.objects.first()
    return dict(topnav=topnav)
    
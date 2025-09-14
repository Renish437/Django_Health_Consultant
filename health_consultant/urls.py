
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    # about 
    path('about/',views.about,name="about"),
    path('about-health-coach/',views.aboutHealthCoach,name="about-health-coach"),
    path('admin/', admin.site.urls),
    path('services/',views.services,name='services'),
    path('events/',views.events,name='events'),
    path('contacts/',views.contacts,name='contacts'),
    path('testimonials/',views.testimonials,name='testimonials'),
    path('projects/',views.projects,name='projects'),
    path('faqs/',views.faqs,name="faqs"),
    path('account/',views.accounts,name="accounts"),
    
    path('shop/',include('shop.urls')),
    path('blog/',include('blog.urls')),
    
    
    
 
]

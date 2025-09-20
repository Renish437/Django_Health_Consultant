
from django.shortcuts import HttpResponse,render
from myapp.models import *

def home(request):
    sliders = Slider.objects.all()
    context = {
        'sliders':sliders
    }
    return render(request,'home/home.html',context)

def about(request):
    return render(request,'about/about.html')
def aboutHealthCoach(request):
    return render(request,'about/about-health-coach.html')

def services(request):
    return render(request,'services/services.html')

def events(request):
    return render(request,'events/events.html')

def contacts(request):
    return render(request,'contacts/contacts.html')
def testimonials(request):
    return render(request,'testimonials/testimonials.html')
def projects(request):
    return render(request,'projects/projects.html')
def faqs(request):
    return render(request,'faqs/faqs.html')

def accounts(request):
    return render(request,'accounts/accounts.html')
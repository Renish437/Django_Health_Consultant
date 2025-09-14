
from django.shortcuts import HttpResponse,render


def home(request):
    return render(request,'home/index.html')

def about(request):
    return render(request,'about/index.html')
def aboutHealthCoach(request):
    return render(request,'about/about-health-coach.html')

def services(request):
    return render(request,'services/index.html')

def events(request):
    return render(request,'events/index.html')

def contacts(request):
    return render(request,'contacts/index.html')
def testimonials(request):
    return render(request,'testimonials/index.html')
def projects(request):
    return render(request,'projects/index.html')
def faqs(request):
    return render(request,'faqs/index.html')

def accounts(request):
    return render(request,'accounts/index.html')
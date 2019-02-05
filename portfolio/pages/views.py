from django.shortcuts import render
from .models import Job
# Create your views here.
def home(request):
    Jobs = Job.objects
    return render(request, 'pages/home.html', {'jobs': Jobs})

def contact(request):
    return render(request, 'pages/contact.html')
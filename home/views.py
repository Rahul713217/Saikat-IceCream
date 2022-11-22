from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')


def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        # password = request.POST.get('password')
        desc = request.POST.get('desc')
        file = request.POST.get('file')
        contact = Contact(name=name, phone=phone, email=email, password=password, desc=desc, file=file, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message is sent successfully!')

    return render(request,'contact.html')


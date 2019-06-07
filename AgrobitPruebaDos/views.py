from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse


def index(request):
    # return HttpResponse('index')
    return render(request,'index.html')

def login_redirect(request):
     return redirect(reverse('login'))


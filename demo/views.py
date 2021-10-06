from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'demo/user-login.html')


def signIn(request):
    return render(request, 'demo/user-login.html')


def signUp(request):
    return render(request, 'demo/user-register.html')


def dashboard(request):
    return render(request, 'demo/index.html')


def tenderSubmission(request):
    return render(request, 'demo/tender-submission.html')

    
    
    

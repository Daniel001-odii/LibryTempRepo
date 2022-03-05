
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def upload(request):
    return render(request, 'upload.html')

def logout(request):
    return render(request, 'registration/libry.html')

def signUp(request):
    return render(request, 'registration/signUp.html')

def reset(request):
    return render(request, 'registration/reset.html')

def profile(request):
    return render(request, 'profile.html')
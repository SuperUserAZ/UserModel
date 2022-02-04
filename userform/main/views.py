from django.shortcuts import render, redirect
from .models import userData
from .forms import userDataForm

def index(request):
    return render(request, 'main/index.html')


def login(request):
    return render(request, 'main/login.html')


def signup(request):
    
    error = ''
    if request.method == 'POST':
        form = userDataForm(request.POST)
        if form.is_valid():
            print("true")
            form.save()
            return redirect('profile')
        else: 
            error = 'form data was entered incorrectly'
    form = userDataForm
    context = {
        'form': form,
        'error': error
    }

    return render(request, 'main/signup.html')


def profile(request):
    return render(request, 'main/profile.html')
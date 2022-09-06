from django.shortcuts import render, redirect
from .models import Room
from .forms import Dataform
from django.contrib.auth.forms import UserCreationForm

def createuser(request):
    if request.method == 'POST':
        user = UserCreationForm(request.POST)
        if user.is_valid():
            user.save()
            return redirect('register')
    else:
        user = UserCreationForm()
    return render(request, 'pages/user.html', {'forms': user})

def home(request):
    rooms = Room.objects.all()
    context = {
        "rooms": rooms,
    }
    return render(request, 'pages/home.html', context)

def f(request):
    if request.method=='POST':
        form = Dataform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base-home')
    else:
        form = Dataform()
    return render(request, 'pages/register.html', {'form': form})
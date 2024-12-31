from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import BusCard
from .forms import RegisterForm
from datetime import date, timedelta

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            BusCard.objects.create(
                user=user,
                expiry_date=date.today() + timedelta(days=365)  # 1-year validity
            )
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def manage_card(request):
    card = BusCard.objects.get(user=request.user)
    return render(request, 'manage_card.html', {'card': card})

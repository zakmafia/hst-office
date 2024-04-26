from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterationForm
from .models import Account

def login(request):
    if request.user.is_authenticated:
        return redirect('bookings')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        email = email.strip()
        
        print(email, password)
        user = auth.authenticate(email=email, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            messages.success(request, f'You are successfully logged in {user.username}')
            return redirect(request.GET['next'] if 'next' in request.GET else 'bookings')
        else:
            messages.error(request, f'You are not a valid user!')
    return render(request, 'accounts/login.html')

def register(request):
    form = RegisterationForm()
    if request.user.is_authenticated:
        return redirect('bookings')
    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username, _ = email.split('@') 
            user = Account.objects.create_user(email=email, password=password, username=username)
            user.save()
            return redirect('bookings')
        else:
            messages.error(request, f'User with the same email exists!')
    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')
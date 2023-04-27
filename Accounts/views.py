from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.


def register(request):
    if request.method == 'POST':
        data = request.POST
        first_name = data['first_name']
        last_name = data['last_name']
        username = data['username']
        email = data['email']
        password = data['password']
        confirm_password = data['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect('Accounts:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect('Accounts:register')
            else:
                user = User.objects.create(username=username, password=password,
                                           email=email, first_name=first_name, last_name=last_name)
                user.save()
                return redirect('Accounts:login_user')
        else:
            messages.info(request, 'Password not matching!')
            return redirect('Accounts:register')
    else:
        return render(request, 'Accounts/register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('Accounts:login_user')

    else:
        return render(request, 'Accounts/login.html')
    
def home(request):
    return render(request,'home.html')

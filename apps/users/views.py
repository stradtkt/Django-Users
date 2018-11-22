from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .forms import *
from .models import *
import bcrypt
# Create your views here.


def index(request):
    return render(request, 'users/index.html', {})

def login(request):
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.filter(email=email)
    if len(user) > 0:
        is_pass = bcrypt.checkpw(password.encode('utf-8'), user[0].password.encode('utf-8'))
        if is_pass:
            request.session['id'] = user[0].id
            return redirect('users:dashboard')
        else:
            messages.error(request, "Incorrect email and/or password")
            return redirect('users:home')
    else:
        messages.error(request, "User does not exist")
    return redirect('users:home')

def register(request):
    errors = User.objects.validate_user(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error)
        return redirect('users:home')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        image = request.POST['image']
        password = request.POST['password']
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        User.objects.create(first_name=first_name, last_name=last_name, image=image, username=username, email=email, password=hashed_pw)
        return redirect('users:login_page')

def logout(request):
    request.session.clear()
    return redirect('users:home')


def login_page(request):
    form = LoginForm()
    context = {
        "form": form
    }
    return render(request, 'users/login.html', context)

def register_page(request):
    form = RegisterForm()
    context = {
        "form": form
    }
    return render(request, 'users/register.html', context)

def dashboard(request):
    try:
        request.session['id']
    except KeyError:
        return redirect('users:home')

    if 'id' in request.session == None:
        return redirect('users:home')
    users = User.objects.all()
    context = {
        "users": users
    }
    return render(request, 'users/dashboard.html', context)

def delete_user(request, id):
    try:
        request.session['id']
    except KeyError:
        return redirect('users:home')

    if 'id' in request.session == None:
        return redirect('users:home')
    user = User.objects.get(id=id)
    user.delete()
    messages.success(request, 'User Deleted')
    return redirect('users:dashboard')

def profile(request, id):
    try:
        request.session['id']
    except KeyError:
        return redirect('users:home')

    if 'id' in request.session == None:
        return redirect('users:home')
    user = User.objects.get(id=id)
    context = {
        "user": user
    }
    return render(request, 'users/profile.html', context)

def send_message(request, id):
    errors = Message.objects.validate_message(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error)
        return redirect(reverse("users:profile", kwargs={'id': id}))
    else:
        receiver = User.objects.get(id=id)
        sender = User.objects.get(id=request.session['id'])
        content = request.POST['content']
        Message.objects.create(receiver=receiver, sender=sender, content=content)
        messages.success(request, 'Sent message')
        return redirect(reverse('users:profile', kwargs={'id': id}))



from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.core.paginator import Paginator
from .forms import *
from .models import *
from userprofile.models import Customer


# Create your views here.

def home(request):
    top = Product.objects.filter(topselling=True)
    feature = Product.objects.filter(featured=True)
    
    cate = Category.objects.all()

    context = {
        'top': top,
        'feature': feature,
        'cate': cate,
        
     }
    return render(request, 'index.html', context)

def products(request):
    yes = Product.objects.all()
    p = Paginator(yes, 8)
    page = request.GET.get('page')
    pagin = p.get_page(page)

    

    context ={
        'pagin': pagin,
        

    }
    return render(request, 'products.html',context)

def detail(request,id):
    prodet = Product.objects.get(pk = id)

    context = {
        'prodet': prodet,
    }
    return render(request, 'detail.html', context) 

def category(request, id, slug):
    catname = Category.objects.get(pk=id)
    cate = Product.objects.filter(category_id = id)

    context = {
        'catname':catname,
        'cate':cate,
    }

    return render(request, 'category.html', context)

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent')
            return redirect('home')
        else:
            messages.error(request, form.errors)
            return redirect('contact')
    context = {
        'form': form,
    }
            
    return render(request, 'contact.html', context)

def signout(request):
    logout(request)
    messages.success(request, 'You are now signed out')
    return redirect('home')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Welcome Chidi')
            return redirect('home')
        else:
            messages.info(request, 'username/password incorrect')
            return redirect('signin')

    return render(request, 'login.html')

def register(request):
    customer = CustomerForm()
    if request.method == 'POST':
        phone = request.POST['phone']
        address = request.POST['address']
        pix = request.POST['pix']
        customer = CustomerForm(request.POST)
        if customer.is_valid():
            user = customer.save()
            newuser = Customer()
            newuser.user = user
            newuser.first_name = user.first_name
            newuser.last_name = user.last_name
            newuser.email = user.email
            newuser.phone = phone
            newuser.address = address
            newuser.pix = pix
            newuser.save()
            messages.success(request, f'Dear {user} your account has been created successfully')
            return redirect('signin')
        else:
            messages.error(request, customer.errors)
            return redirect('register')

    return render(request, 'register.html')

def profile(request):
    userprof = Customer.objects.get(user__username=request.user.username)

    context = {
        'userprof':userprof
    }

    return render(request, 'profile.html', context)

def profile_update(request):
    userprof = Customer.objects.get(user__username=request.user.username)
    profile = ProfileForm(instance=request.user.customer)
    if request.method == 'POST':
        profile = ProfileForm(request.POST, request.FILES, instance=request.user.customer)
        if profile.is_valid():
            pupdate = profile.save()
            new = pupdate.first_name
            messages.success(request, f'dear{new} your profile update is successful')
            return redirect('profile')
        else:
            messages.error(request, f'dear{new} your profile update generated the following errors: {profile.errors}')
            return redirect('profile_update')
    context = {
        'userprof':userprof
    }

    return render(request, 'profile_update.html', context)


def password_update(request):
    userprof = Customer.objects.get(user__username=request.user.username)
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            newpass = form.save()
            update_session_auth_hash(request, newpass)
            messages.success(request, 'password changed successfully')
            return redirect('profile')
        else:
            messages.error(request, f'the following errors were encountered: {form.errors}')
            return redirect('password_update')
    
    context = {
        'userprof':userprof,
        'form':form,
    }

    return render(request, 'password_update.html', context)

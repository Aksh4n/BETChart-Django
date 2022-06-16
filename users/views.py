from gc import get_objects
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm , WalletAddressForm 
from verify_email.email_handler import send_verification_email
from django.utils.safestring import mark_safe
from .models import UserBankAccount
from django.contrib.auth.models import User
from django.db import models



# Create your views here.
def login_user(request):
    if request.method == "POST" :
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
            # Redirect to a success page.
            
        else:
            messages.success(request, ("There was an Error loging in, try again..."))
            return redirect('login')
            # Return an 'invalid login' error message.
            

    else:
        return render(request, 'authenticate/users.html' , {})


def logout_user(request):
    logout(request)
    messages.success(request, ("you were logged out"))
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid() :
            inactive_user = send_verification_email(request, form)
            
            
            messages.success(request, mark_safe('registeration successful , please verify your email and log in .. if you didnt get the email<a href="http://127.0.0.1:8000/verification/user/verify-email/request-new-link/">click here to resend</a>'))
            return redirect('login')
    else:
        form = RegisterUserForm()    
    return render(request, 'authenticate/register_user.html', {       
        'form':form,
    })
def profile(request):

    return render(request, 'profile.html' , {})    

def walletaddress(request):
    if request.method == "POST":
        
        walletaddress = UserBankAccount.objects.get(id=request.user.account.id)
        f = WalletAddressForm(request.POST, instance=walletaddress)
        f.save()
            
        messages.success(request, ('We got your wallet address for withdrawal successfully!'))
        return redirect('walletaddress')
    else:
        form = WalletAddressForm()    
    return render(request, 'walletaddress.html', {       
        'form':form,
    })


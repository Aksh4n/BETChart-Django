from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from .models import Contact
from django.contrib.auth.decorators import login_required



@login_required()

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid() :
            form.save()
            
            messages.success(request, ('We got your message , we will get in touch with you through  your email address ASAP!'))
            return redirect('contact')
    else:
        form = ContactForm()    
    return render(request, 'contact.html', {       
        'form':form,
    })

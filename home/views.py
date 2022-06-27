from django.shortcuts import render
from transactions.models import CurrentPrice

# Create your views here.
def home(request):
    return render(request, 'home.html' , {})


def rules(request):
    price = CurrentPrice.objects.get(id=1).price
    return render(request, 'rules.html' , {
        'price':price,
        })   

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from transactions.views import TransactionCreateMixin
from django.contrib import messages
from transactions.constants import BETRED
from transactions.forms import Bet


# Create your views here.
@login_required()
def game(request):
    return render(request, 'game.html' , {})

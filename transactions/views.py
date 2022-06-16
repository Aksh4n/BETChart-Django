from dateutil.relativedelta import relativedelta
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, ListView
from django.contrib.auth.decorators import login_required

from transactions.constants import DEPOSIT, WITHDRAWAL, BETRED, BETGREEN
from transactions.forms import (
    DepositForm,
    TransactionDateRangeForm,
    WithdrawForm, Bet 
)
from transactions.models import Transaction, Pot , GreenMember , RedMember


class TransactionRepostView(LoginRequiredMixin, ListView):
    template_name = 'transactions/transaction_report.html'
    model = Transaction
    form_data = {}

    def get(self, request, *args, **kwargs):
        form = TransactionDateRangeForm(request.GET or None)
        if form.is_valid():
            self.form_data = form.cleaned_data

        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset().filter(
            account=self.request.user.account
        )

        daterange = self.form_data.get("daterange")

        if daterange:
            queryset = queryset.filter(timestamp__date__range=daterange)

        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'account': self.request.user.account,
            'form': TransactionDateRangeForm(self.request.GET or None)
        })

        return context


class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    template_name = 'transactions/transaction_form.html'
    model = Transaction
    title = ''
    success_url = reverse_lazy('transactions:transaction_report')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'account': self.request.user.account
        })
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': self.title
        })

        return context


class DepositMoneyView(TransactionCreateMixin):
    form_class = DepositForm
    title = 'Deposit Money to Your Account'

    def get_initial(self):
        initial = {'transaction_type': DEPOSIT}
        return initial

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account

        if not account.initial_deposit_date:
            now = timezone.now()
            account.initial_deposit_date = now
            

        account.balance += amount
        account.save(
            update_fields=[
                'initial_deposit_date',
                'balance',
                
            ]
        )

        messages.success(
            self.request,
            f'{amount}$ was deposited to your account successfully'
        )

        return super().form_valid(form)


class WithdrawMoneyView(TransactionCreateMixin):
    form_class = WithdrawForm
    title = 'Withdraw Money from Your Account'

    def get_initial(self):
        initial = {'transaction_type': WITHDRAWAL}
        return initial

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')

        self.request.user.account.balance -= form.cleaned_data.get('amount')
        self.request.user.account.save(update_fields=['balance'])

        messages.success(
            self.request,
            f'Successfully withdrawn {amount}$ from your account'
        )

        return super().form_valid(form)

class TransactionCreateMixinBet(LoginRequiredMixin, CreateView):
    template_name = 'game.html'
    model = Transaction 
    title = ''
    success_url = reverse_lazy('transactions:bet_money')
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'account': self.request.user.account ,
            
        })
        return kwargs

    def get_context_data(self, **kwargs):
        j =  Pot.objects.get(id=1).pot - 5
        context = super().get_context_data(**kwargs)
        context.update({
            'title': self.title ,
            'data' : j  ,
            'type': GreenMember.objects.filter(g=0).exclude(account_id=3) ,
            'type1': RedMember.objects.filter(g=0).exclude(account_id=3) ,

            
        })

        return context


class BetMoneyView(TransactionCreateMixinBet):
    form_class = Bet 
    title = 'place a bet'
    


    def get_initial(self):
    


        initial = {'transaction_type': BETRED}
    


        return initial

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')


        self.request.user.account.balance -= form.cleaned_data.get('amount')
        self.request.user.account.save(update_fields=['balance'])
        


        

        return super().form_valid(form)

        #GREEN


class BetMoneyView2(TransactionCreateMixinBet):
    form_class = Bet 
    title = 'place a bet'
    


    def get_initial(self):
    


        initial = {'transaction_type': BETGREEN}
    


        return initial

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')


        self.request.user.account.balance -= form.cleaned_data.get('amount')
        self.request.user.account.save(update_fields=['balance'])
        


        

        return super().form_valid(form)









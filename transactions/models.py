from django.db import models
from requests import request

from .constants import TRANSACTION_TYPE_CHOICES , BETGREEN
from users.models import UserBankAccount
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from datetime import datetime
import time
from time import time, sleep





class Transaction(models.Model):
    account = models.ForeignKey(
        UserBankAccount,
        related_name='transactions',
        on_delete=models.CASCADE,
    )
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=12
    )
    balance_after_transaction = models.DecimalField(
        decimal_places=2,
        max_digits=12
    )
    transaction_type = models.PositiveSmallIntegerField(
        choices=TRANSACTION_TYPE_CHOICES , 
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.account.user)

    class Meta:
        ordering = ['-timestamp']
        get_latest_by = "timestamp"



class Pot(models.Model):
    pot = models.DecimalField(decimal_places=2,max_digits=12)


    def __str__(self):

        return str(self.pot)



    def __call__(self):

        return self    
    

def update_pot(sender, instance, created, **kwargs):

    transaction_type = Transaction.objects.latest().transaction_type
    


    if created:

        if transaction_type == 3:

            a = Pot.objects.get(id=1).pot + 5
            Pot.objects.update(pot=a)
        elif transaction_type == 4:
            a = Pot.objects.get(id=1).pot + 5
            Pot.objects.update(pot=a)

            


       
       

post_save.connect(update_pot, sender=Transaction)




class GreenMember(models.Model):
    account = models.ForeignKey(
        User,
        related_name='greenmembers',
        on_delete=models.CASCADE,
    )

    g = models.PositiveSmallIntegerField(default=0, null=True)
    a = models.CharField(max_length=200 , null=True)


    def __str__(self):
        return str(self.account)


def add_green_member(sender, instance, created, **kwargs):
    transaction_type = Transaction.objects.latest().transaction_type


    if created:

        if transaction_type == 4 :
            


            GreenMember.objects.create(account=instance.account.user , a=instance.account.user)

post_save.connect(add_green_member, sender=Transaction)


class RedMember(models.Model):
    account = models.ForeignKey(
        User,
        related_name='redmembers',
        on_delete=models.CASCADE,
    )
    g = models.PositiveSmallIntegerField(default=0 , null=True)
    a = models.CharField(max_length=200 , null=True)



    def __str__(self):
        return str(self.account)


def add_red_member(sender, instance, created, **kwargs):
    transaction_type = Transaction.objects.latest().transaction_type


    if created:

        if transaction_type == 3 :
            


            RedMember.objects.create(account=instance.account.user , a=instance.account.user)

post_save.connect(add_red_member, sender=Transaction)


class CurrentPrice(models.Model):


    price = models.DecimalField(decimal_places=2,max_digits=12)

    def __str__(self):

        return str(self.price)




class CandleColor(models.Model):

    color = models.PositiveSmallIntegerField()

    class Meta:

        get_latest_by = "id"

   


def e_bet(sender, instance, created, **kwargs):

    candlecolor1 = CandleColor.objects.latest().color
    redmembers1 = RedMember.objects.filter(g=0)
    greenmembers1 = GreenMember.objects.filter(g=0)
    redcount = RedMember.objects.all().count()
    greencount = GreenMember.objects.all().count()
    prize = Pot.objects.get(id=1).pot
    sarsh = User.objects.get(id=1)


    if created:

        if candlecolor1 == 1:
            if greencount > 0:

                q = prize / greencount 
                for user in greenmembers1 :
                    user.account.account.balance += q 
                user.account.account.save(update_fields=['balance'])   
                GreenMember.objects.all().delete()
                RedMember.objects.all().delete()
                Pot.objects.update(pot=0)
                MemberCount.objects.update(gc=0 , rc=0)
            elif greencount == 0 :
                GreenMember.objects.all().delete()
                RedMember.objects.all().delete()
                Pot.objects.update(pot=0)
                MemberCount.objects.update(gc=0 , rc=0)

        elif candlecolor1 == 2 :
            if redcount > 0 :

                q = prize / redcount 
                for user in redmembers1 :
                    user.account.account.balance += q 
                user.account.account.save(update_fields=['balance'])   
                GreenMember.objects.all().delete()
                RedMember.objects.all().delete()
                Pot.objects.update(pot=0) 
                MemberCount.objects.update(gc=0 , rc=0)
            elif redcount == 0 :
                GreenMember.objects.all().delete()
                RedMember.objects.all().delete()
                Pot.objects.update(pot=0)
                MemberCount.objects.update(gc=0 , rc=0) 





        
post_save.connect(e_bet, sender=CandleColor)






class MemberCount(models.Model):
    gc = models.IntegerField(default=0 , null=True)
    rc = models.IntegerField(default=0 , null=True)

def update_count(sender, instance, created, **kwargs):

    
    if created:


        a = GreenMember.objects.all().count()
        b = RedMember.objects.all().count()
        MemberCount.objects.update(gc=a , rc=b)

post_save.connect(update_count, sender=GreenMember)
post_save.connect(update_count, sender=RedMember)



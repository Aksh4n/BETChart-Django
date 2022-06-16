from django.db import models
from . import errors

from django.contrib.auth.models import User
from django.db import models, transaction
from django.db.models.signals import post_save



class UserBankAccount(models.Model):
    user = models.OneToOneField(
        User,
        related_name='account',
        on_delete=models.CASCADE,
    )

    account_no = models.PositiveIntegerField(unique=True , null=True)
    balance = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2
    )
    initial_deposit_date = models.DateField(null=True, blank=True)

    walletaddress = models.CharField(max_length=300, null=True, blank=True)    
    


    def __str__(self):
        return str(self.user.username)   


    def __call__(self):
        return self    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserBankAccount.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)


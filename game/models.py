from django.db import models

# Create your models here.
class TotalPot(models.Model):
    pot = models.DecimalField(
    default=0,
    max_digits=12,
    decimal_places=2
    )

from django.db import models

# Create your models here.
class Contact(models.Model):
    subject = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=1000)



    def __str__(self):

        return self.email + '' + self.subject  

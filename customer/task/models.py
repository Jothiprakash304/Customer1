from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Register_customer(models.Model):
    Email=models.EmailField(max_length=100,unique=True)
    Name=models.CharField(max_length=100,unique=True)
    class Meta:
        db_table="Register_customer"

# @receiver(post_save,sender=settings.AUTH_USER_MODEL)
# def function(sender,instance=None,created=False,**kwargs):
#     if created:
#         Token.objects.create(user=instance) 
from django.db import models

# Create your models here.
class Register_customer_1(models.Model):
    Email=models.EmailField(max_length=100,unique=True)
    Name=models.CharField(max_length=100,unique=True)
    class Meta:
        db_table="Register_customer_1"
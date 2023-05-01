from rest_framework import serializers
from .models import Register_customer
from django.core.exceptions import ValidationError



class Register_serializer(serializers.ModelSerializer):
    class Meta:
        model=Register_customer
        fields=['Email','Name']

class Register_update(serializers.ModelSerializer):
    class Meta:
        model=Register_customer
        fields=["Email","Name"]
    # def create(self,data):
    #     user=

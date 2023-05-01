from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import Register_customer_1




class Register_serializer_1(serializers.ModelSerializer):
    class Meta:
        model=Register_customer_1
        fields=['id','Email','Name']
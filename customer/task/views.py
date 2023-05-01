from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Register_customer
import requests
import json
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.auth.models import User
from .serializers import Register_serializer,Register_update
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def Register(request):
    validate=Register_serializer(data=request.data)
    if validate.is_valid():
           validate.save()
           Email=validate.data['Email']
           Name=validate.data['Name']
           user=User.objects.create_user(username=Email,password=Name)
           token=Token.objects.create(user=user)
           request.session['token']=token.key
           data={
                "Email":Email,
                "Name":Name
           }
           json_data=json.dumps(data)
           headers = {
                'Authorization':'Token '+ token.key,
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'User-Agent': 'my-app/1.0',
           }
           response=requests.post('http://127.0.0.1:8000/api4',headers=headers,data=json_data)
           response.raise_for_status()
           return Response(validate.data)
    
@api_view(['PUT'])
def Update(request,pk):
    my_model=Register_customer.objects.get(Email=pk)
    serializer=Register_update(my_model,data=request.data)
    if serializer.is_valid():
        serializer.save()
        Email=serializer.data['Email']
        Name=serializer.data['Name']
        user=User.objects.create_user(username=Email,password=Name)
        token=Token.objects.create(user=user)
        data={
                "Email":Email,
                "Name":Name
           }
        json_data=json.dumps(data)
        headers = {
                'Authorization':'Token '+ token.key,
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'User-Agent': 'my-app/1.0',
           }
        response=requests.put('http://127.0.0.1:8000/api5/{}'.format(pk),headers=headers,data=json_data)
        response.raise_for_status()
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def Delete(request,pk):
    token=request.session.get('token')
    if token:
       headers={
               'Authorization': 'Token ' + token
          }
    response=requests.delete('http://127.0.0.1:8000/api6/{}'.format(pk),headers=headers)
    response.raise_for_status()
    return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['GET'])
def get(request,pk):
     token=request.session.get('token')
     if token:
          headers={
               'Authorization': 'Token ' + token
          }
          response=requests.get('http://127.0.0.1:8000/api7/{}'.format(pk),headers=headers)
          response.raise_for_status()
          return Response(response.json())
     else:
          return Response({'error':'Authentication required'},status=status.HTTP_401_UNAUTHORIZED)
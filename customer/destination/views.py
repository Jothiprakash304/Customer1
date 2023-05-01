from django.shortcuts import render,HttpResponse
from django.http import HttpResponseBadRequest,JsonResponse
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import generics
import json
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Register_customer_1
from rest_framework.authtoken.models import Token
from .serializers import Register_serializer_1


# Create your views here.
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def web(request):
    serializer=Register_serializer_1(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def put(request,pk):
    s=Register_customer_1.objects.get(Email=pk)
    serializer_1=Register_serializer_1(s,data=request.data)
    if serializer_1.is_valid():
        serializer_1.save()
        return Response(serializer_1.data)
    
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get(request,pk):
    get=Register_customer_1.objects.get(Email=pk)
    serializer=Register_serializer_1(get)
    return Response(serializer.data)


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete(request,pk):
    s=Register_customer_1.objects.filter(Email=pk)
    s.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


    

"""
from django.shortcuts import render
from .models import Aiquest
from .serializer import AiquestSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
"""
from .models import Aiquest
from .serializer import AiquestSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

class Aiquest_List_Create(ListCreateAPIView):
    queryset=Aiquest.objects.all()
    serializer_class=AiquestSerializer
    
    
class Aiquest_Retrive_Update_Destroy(RetrieveUpdateDestroyAPIView):
    queryset=Aiquest.objects.all()
    serializer_class=AiquestSerializer
    
    
    

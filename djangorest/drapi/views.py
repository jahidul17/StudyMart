"""
from django.shortcuts import render
from .models import Aiquest
from .serializer import AiquestSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
"""
from .models import Aiquest
from .serializer import AiquestSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

class Aiquest_Model_View_Set(viewsets.ModelViewSet):
    #List, Create, Delete, Update, Partial Update
    queryset=Aiquest.objects.all()
    serializer_class=AiquestSerializer
    
    # permission_classes=[IsAdminUser]
    

    
    
    

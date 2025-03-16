from django.shortcuts import render
from .models import Aiquest
from .serializer import AiquestSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET','POST','PUT','PATCH','DELETE'])
def aiquest_create(request,pk=None):
    if request.method=='GET':
        id=pk
        if id is not None:
            #complex data
            ai=Aiquest.objects.get(id=id)
            #python dict
            serializer=AiquestSerializer(ai)
            return Response(serializer.data)
        
        #complex data
        ai=Aiquest.objects.all()
        #python dict
        serializer=AiquestSerializer(ai,many=True)
        return Response(serializer.data)
        
    if request.method=='POST':
        serializer=AiquestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Successfully insert data'})
        return Response(serializer.errors)

    if request.method == 'PUT':
        id=pk
        ai=Aiquest.objects.get(pk=id)
        serializer=AiquestSerializer(ai,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Full data update'})
        return Response(serializer.errors)
    
    
    if request.method == 'PATCH':
        id=pk
        ai=Aiquest.objects.get(pk=id)
        serializer=AiquestSerializer(ai,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial data updated'})
        return Response(serializer.errors)


    if request.method=='DELETE':
        id=pk
        ai=Aiquest.objects.get(pk=id)
        ai.delete()
        return Response({'msg':'Successfully deleted data'})
        




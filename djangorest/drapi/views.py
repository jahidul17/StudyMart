from django.shortcuts import render
from .models import Aiquest
from .serializer import AiquestSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser

# Create your views here.

def aiquest_info(request):
    #complex data
    ai=Aiquest.objects.all()
    #python dict
    serializer=AiquestSerializer(ai,many=True)
    #render Json
    json_data=JSONRenderer().render(serializer.data)
    #json sent to user
    return HttpResponse(json_data,content_type='application/json')



#Model Instance
def aiquest_ins(request,pk):
    #complex data
    ai=Aiquest.objects.get(id=pk) 
    #python dict
    serializer=AiquestSerializer(ai)
    #render Json
    json_data=JSONRenderer().render(serializer.data)
    #json sent to user
    return HttpResponse(json_data,content_type='application/json')


@csrf_exempt
def aiquest_create(request):
    if request.method == 'POST':
        json_data=request.body
        #json to stram convert
        stream=io.BytesIO(json_data)
        #stream to python
        pythondata=JSONParser().parse(stream)
        #python to complex
        serializer=AiquestSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Successfully insert data.'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application.json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application.json')
    
    
    if request.method == 'PUT':
        json_data=request.body
        #json to stream
        stream=io.BytesIO(json_data)
        #stream to python
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        aiq=Aiquest.objects.get(id=id)
        serializer=AiquestSerializer(aiq,data=pythondata,partial=True) #if partial data update partial=true otherwise haven't
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Successfully Update data'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application.json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application.json')
    
    
    if request.method=='DELETE':
        json_data=request.body
        #json to stream
        stream=io.BytesIO(json_data)
        #stream to python
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        aiq=Aiquest.objects.get(id=id)
        
        aiq.delete()
        res={'msg':'Successfully delete data'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application.json')
        
"""
from django.shortcuts import render
from .models import Aiquest
from .serializer import AiquestSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
"""
from .models import Aiquest
from .serializer import AiquestSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin


# class AiquestList(GenericAPIView,ListModelMixin):
#     queryset=Aiquest.objects.all()
#     serializer_class=AiquestSerializer
    
#     def get(self,request,*args, **kwargs):
#         return self.list(request,*args,**kwargs)
    

# class AiquestCreate(GenericAPIView,CreateModelMixin):
#     queryset=Aiquest.objects.all()
#     serializer_class=AiquestSerializer
    
#     def post(self,request,*args, **kwargs):
#         return self.create(request,*args,**kwargs)
    
#Combine above class
class Aiquest_List_Create(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Aiquest.objects.all()
    serializer_class=AiquestSerializer
    
    def get(self,request,*args, **kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args, **kwargs):
        return self.create(request,*args,**kwargs)
    
    
    
    
# class AiquestRetrive(GenericAPIView,RetrieveModelMixin):
#     queryset=Aiquest.objects.all()
#     serializer_class=AiquestSerializer
    
#     def get(self,request,*args, **kwargs):
#         return self.retrieve(request,*args, **kwargs)
    

# class AiquestUpdate(GenericAPIView,UpdateModelMixin):
#     queryset=Aiquest.objects.all()
#     serializer_class=AiquestSerializer
    
#     def put(self,request,*args, **kwargs):
#         return self.update(request,*args, **kwargs)



# class AiquestDestroy(GenericAPIView,DestroyModelMixin):
#     queryset=Aiquest.objects.all()
#     serializer_class=AiquestSerializer
    
#     def delete(self,request,*args, **kwargs):
#         return self.destroy(request,*args, **kwargs)


#Combine above class

class Aiquest_Retrive_Update_Destroy(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=Aiquest.objects.all()
    serializer_class=AiquestSerializer
    
    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    
    
    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)

    
    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)


"""
class AiquestCreate(APIView):  
    def get(self,request,pk=None,format=None):
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
        
    def post(self,request,format=None):
        serializer=AiquestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Successfully insert data'})
        return Response(serializer.errors)

    def put(self,request,pk,format=None):
        id=pk
        ai=Aiquest.objects.get(pk=id)
        serializer=AiquestSerializer(ai,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Full data update'})
        return Response(serializer.errors)
    
    
    def patch(self,request,pk,format=None):
        id=pk
        ai=Aiquest.objects.get(pk=id)
        serializer=AiquestSerializer(ai,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial data updated'})
        return Response(serializer.errors)


    def delete(self,request,pk,format=None):
        id=pk
        ai=Aiquest.objects.get(pk=id)
        ai.delete()
        return Response({'msg':'Successfully deleted data'})
"""        
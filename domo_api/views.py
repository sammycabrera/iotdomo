from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from domo_api.models import *
from domo_api.serializers import *
# Create your views here.
# https://blog.logrocket.com/django-rest-framework-create-api/


class Locations_Id_method(APIView):
    def get(self, request):
        locations=Locations.objects.all()
        content ={}
        #locations_list=[]
        #for i in locations:
        #    locations_list.append({"id":i.id,"name_location":i.name_location,"user_id":i.user_id})
        #content["locations"]=locations_list
        locations_list= LocationSerializer(locations,many=True).data
        content["locations"]=locations_list
        return Response(content, status=status.HTTP_200_OK)
    

class Locations_method(APIView):
    def post(self, request):
        name_location=request.data["name_location"]
        user=request.data["user_id"]

        location=Locations.objects.create(name_location=name_location,user_id=user)
        return Response("Created location iot",status=status.HTTP_200_OK)


    def get(self, request, codigo):
        locations=Locations.objects.filter(user_id=codigo)
        #locations=Locations.objects.all()
        content ={}
        #locations_list=[]
        #for i in locations:
        #    locations_list.append({"id":i.id,"name_location":i.name_location,"user_id":i.user_id})
        #content["locations"]=locations_list
        locations_list= LocationSerializer(locations,many=True).data
        content["locations"]=locations_list
        return Response(content, status=status.HTTP_200_OK)
    
    def get3(self, request):
        locations=Locations.objects.all()
        content ={}
        #locations_list=[]
        #for i in locations:
        #    locations_list.append({"id":i.id,"name_location":i.name_location,"user_id":i.user_id})
        #content["locations"]=locations_list
        locations_list= LocationSerializer(locations,many=True).data
        content["locations"]=locations_list
        return Response(content, status=status.HTTP_200_OK)

    
    def put(self, request, codigo):
        location=Locations.objects.get(id=codigo)
        location.name_location=request.data["name_location"]
        location.save()        
        return Response("Updated location iot",status=status.HTTP_200_OK)
    
    def delete(self, request, codigo):
        location=Locations.objects.get(id=codigo)
        location.delete()        
        return Response("Delete location iot",status=status.HTTP_200_OK)
    

class Devices_method(APIView):
    def post(self, request):
        name_device=request.data["name_device"]
        unidad=request.data["unidad"]
        location=request.data["location_id"]

        device=Devices.objects.create(name_device=name_device,unidad=unidad,location_id=location)
        return Response("Created Devices iot",status=status.HTTP_200_OK)


    def get(self, request, codigo):
        devices=Devices.objects.filter(id=codigo)
        content ={}
        devices_list= DeviceSerializer(devices,many=True).data
        content["devices"]=devices_list
        return Response(content, status=status.HTTP_200_OK)
    
    
    
    def put(self, request, codigo):
        device=Devices.objects.get(id=codigo)
        #device.unidad=request.data["unidad"]
        device.name_device=request.data["name_device"]
        device.location_id=request.data["location_id"]
        device.save()        
        return Response("Updated device iot",status=status.HTTP_200_OK)
    
    def delete(self, request, codigo):
        device=Devices.objects.get(id=codigo)
        device.delete()        
        return Response("Delete device iot",status=status.HTTP_200_OK)



class Devices_Id_method(APIView):
    def get(self, request):
        devices=Devices.objects.all()
        content ={}
        devices_list= DeviceSerializer(devices,many=True).data
        content["devices"]=devices_list
        return Response(content, status=status.HTTP_200_OK)
    

class Dots_method(APIView):
    def post(self, request):
        value=request.data["value"]
        device=request.data["device_id"]

        dot=Dots.objects.create(value=value,device_id=device)
        return Response("Created Dots iot",status=status.HTTP_200_OK)


    def get(self, request, codigo):
        dots=Dots.objects.filter(id=codigo)
        content ={}
        dots_list= DotSerializer(dots,many=True).data
        content["dots"]=dots_list
        return Response(content, status=status.HTTP_200_OK)
    
    
    
    def delete(self, request, codigo):
        dot=Dots.objects.get(id=codigo)
        dot.delete()        
        return Response("Delete dot iot",status=status.HTTP_200_OK)
    
class Dots_Id_method(APIView):
    def get(self, request):
        dots=Dots.objects.all()
        content ={}
        dots_list= DotSerializer(dots,many=True).data
        content["dots"]=dots_list
        return Response(content, status=status.HTTP_200_OK)
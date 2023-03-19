from rest_framework.response import Response 
from rest_framework.decorators import api_view
from base.models import Client
from .serializers import ClientSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated,IsAdminUser,BasePermission
from rest_framework import permissions
from rest_framework import views
from rest_framework.response import Response






@api_view(['GET'])
def getallclient(request):
    # authemtication_classes =[BasePermission]
    # permissions = [IsAuthenticated,WritebyAdminonlypermission]
    clients = Client.objects.all()
    serializer = ClientSerializer(clients,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getclient(request,pk):
    clients = Client.objects.get(id=pk)
    serializer = ClientSerializer(clients,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addclient(request):
    serializer = ClientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT','PATCH'])
def updateclient(request,pk):
    if request.method=='PUT':
       clients = Client.objects.get(id=pk)
       serializer = ClientSerializer(instance=clients,data=request.data)

       if serializer.is_valid():
          serializer.save()
       return Response(serializer.data)
    
    if request.method == 'PATCH':
        clients= Client.objects.get(id=pk)
        serializer = ClientSerializer(clients ,data=request.data , partial=True)

        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)




@api_view(['Delete'])
def deleteclient(request,pk):
    client= Client.objects.get(id=pk)
    client.delete()
    
    return Response("Client delete succesfully!")


# @api_view(['GET'])
# def Userlist(request):
# #     Permission = [IsAuthenticated]
#     user= IsAdminUser
#     return Response(Userlist.data)


# @api_view(['POST'])
# def addUser(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

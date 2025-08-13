from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from api_rest.models import Client
from api_rest.serializers import ClientSerializer


@api_view(['GET'])
def get_clients(request):

    if request.method == 'GET':
        clients = Client.objects.all()                           # Get all objects in Client's database (it returns a queryset)

        serializer = ClientSerializer(clients, many=True)        # Serialize the objetcs data into json (Has a 'many' parameter cayse it's a queryset)
        return Response(serializer.data)                         # Return the serialized data
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_client_by_cpf(request, cpf):
    
    if request.method == 'GET':
        try:
            client = Client.objects.get(pk=cpf)

            serializer = ClientSerializer(client)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'PUT', 'DELETE'])
def client_manager(request):
    if request.method == 'POST':
        
        new_client = request.data 

        serializer = ClientSerializer(data=new_client)

        if serializer.is_valid():   # verifica se o serializer é valido e salva o serializer
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

    if request.method == 'PUT':
        
        cpf = request.data['cpf']

        try:
            update_client = Client.objects.get(pk=cpf)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ClientSerializer(update_client, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(status= status.HTTP_400_BAD_REQUEST)
    
    
    if request.method == 'DELETE':
        try:
            client_to_delete = Client.objects.get(pk=request.data['cpf'])
            client_to_delete.delete()
            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


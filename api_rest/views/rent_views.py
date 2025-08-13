from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from api_rest.models import Rent
from api_rest.serializers import RentSerializer


@api_view(['GET'])
def get_rents(request):

    if request.method == 'GET':
        rents = Rent.objects.all()                         

        serializer = RentSerializer(rents, many=True)        
        return Response(serializer.data)                         
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_rent_by_code(request, code):
    
    if request.method == 'GET':
        try:
            rent = Rent.objects.get(code=code)

            serializer = RentSerializer(rent)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(status=status.HTTP_400_BAD_REQUEST)

#verificar no vídeo o jeito e fazer get com vários parâmetros. CPF e código do veículo


@api_view(['POST', 'PUT', 'DELETE'])
def rent_manager(request):
    if request.method == 'POST':
        
        new_rent = request.data 

        serializer = RentSerializer(data=new_rent)

        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

    if request.method == 'PUT':
        
        code = request.data['code']

        try:
            update_rent = Rent.objects.get(pk=code)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = RentSerializer(update_rent, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(status= status.HTTP_400_BAD_REQUEST)
    
    
    if request.method == 'DELETE':
        try:
            rent_to_delete = Rent.objects.get(pk=request.data['code'])
            rent_to_delete.delete()
            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

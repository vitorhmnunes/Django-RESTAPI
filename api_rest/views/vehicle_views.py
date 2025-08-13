from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from api_rest.models import Vehicle
from api_rest.serializers import VehicleSerializer


@api_view(['GET'])
def get_vehicles(request):

    if request.method == 'GET':
        vehicles = Vehicle.objects.all()                         

        serializer = VehicleSerializer(vehicles, many=True)        
        return Response(serializer.data)                         
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_vehicle_by_code(request, code):
    
    if request.method == 'GET':
        try:
            vehicle = Vehicle.objects.get(code=code)

            serializer = VehicleSerializer(vehicle)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'PUT', 'DELETE'])
def vehicle_manager(request):
    if request.method == 'POST':
        
        new_vehicle = request.data 

        serializer = VehicleSerializer(data=new_vehicle)

        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

    if request.method == 'PUT':
        
        code = request.data['code']

        try:
            update_vehicle = Vehicle.objects.get(pk=code)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = VehicleSerializer(update_vehicle, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(status= status.HTTP_400_BAD_REQUEST)
    
    
    if request.method == 'DELETE':
        try:
            vehicle_to_delete = Vehicle.objects.get(pk=request.data['code'])
            vehicle_to_delete.delete()
            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from .serializer import HotelSerializer
from main.models import Hotel

@api_view(['GET'])
@permission_classes([AllowAny])
def hello_world(request):
    person = request.query_params['person']
    return Response({"message": f"Hello, {person.title()}!"})

# hotel
@api_view(['GET'])
@permission_classes([AllowAny])
def hotel_list(request):
    hotels = Hotel.objects.all()
    serializer = HotelSerializer(hotels, context={"request": request}, many=True)
    return Response({'hotels':serializer.data})
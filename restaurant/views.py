from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking, MenuItem
from .serializers import bookingSerializer

from rest_framework import generics
# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class bookingview(APIView):
    def get(self, request):
        items = Booking.objects.all()
        serializer = bookingSerializer(items, many =True)
        return Response(serializer.data)  #Return Json
    
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
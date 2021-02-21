from django.shortcuts import render
from .models import GroceryItem
from .serializers import GroceryItemSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import filters
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

# Create your views here.
def home(request):
    return render(request, 'home.html')

#This method is basically used to add records to a database 
# and get records from a database.
@api_view(["GET", "POST"]) 
def show_list(request):
    if request.method == "GET":
        data = GroceryItem.objects.all()
        serializers = GroceryItemSerializers(data, many = True)
        return Response(serializers.data)
    elif request.method == "POST":
        serializers = GroceryItemSerializers(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class MyPageNumberPagination(PageNumberPagination):
    page_size = 3


class GroceryItemListView(generics.ListAPIView):
    queryset = GroceryItem.objects.all()
    serializer_class = GroceryItemSerializers
    pagination_class = MyPageNumberPagination
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    # filter_backends = [filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['price', 'createdAt']

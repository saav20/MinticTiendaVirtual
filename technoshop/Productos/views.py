from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from Productos.serializers import ProductosSerializer, Producto






# Create your views here.
class ListProductosAPIView(ListAPIView):
    """This endpoint list all of the available Productos from the database"""
    queryset = Producto.objects.all()
    serializer_class = ProductosSerializer

class CreateProductosAPIView(CreateAPIView):
    """This endpoint allows for creation of a Productos"""
    queryset = Producto.objects.all()
    serializer_class = ProductosSerializer

class UpdateProductosAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the Productos to update"""
    queryset = Producto.objects.all()
    serializer_class = ProductosSerializer

class DeleteProductosAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Productos from the database"""
    queryset = Producto.objects.all()
    serializer_class = ProductosSerializer

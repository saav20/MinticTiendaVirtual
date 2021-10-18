from rest_framework import serializers
from Productos.models import Producto

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"



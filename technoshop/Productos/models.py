# from django.db import models
# class Carrito (models.Model):
#     def _init_(self, request):
#         self.request = request
#         self.session = request.session
#         carrito = self.session.get("carrito")
#         if not carrito:
#             carrito= self.session["carrito"] = {}
#         self.carrito = carrito

#     def add(self, productos):
#         if str(productos.id) not in self.carrito.keys():
#             self.carrito[productos.id] = {
#                 "productos_id": productos.id,
#                 "nombre": productos.nombre,
#                 "cantidad": 1,
#                 "precios": str(productos.precios),
#                 #"imagenes": productos.imagenes.url
#             }
#         else:
#             for key, value in self.carrito.items():
#                 if key == str(productos.id):
#                     value["cantidad"] = value["cantidad"] + 1
#         self.save()
#     def save(self):
#         self.session["carritos"] = self.carrito
#         self.session.modified = True  
#     def remove (self, productos):
#         productos_id = str(productos.id)
#         if productos_id in self.carrito:
#             del self.carrito[productos_id]
#             self.save()
#     def decrement(self, productos):
#         for key, value in self.carrito.items():
#             if key == str(productos.id):
#                 value["cantidad"] = value["cantidad"] - 1
#                 if value["cantidad"] < 1:
#                   self.remove(productos)
#                 break
#             else:
#                 print("El pructo se a eliminado de su compra")

#     def clear(self):
#         self.session["carrito"] = {}
#         self.session.modified = True
# from django.db import models
# class Carrito(models.Model):
#       productos = models.CharField(max_length=200)
#       nombre=  models.CharField(max_length=200)
#       cantidad= models.CharField(max_length=200)
#       precio= models.CharField(max_length=200)
#       referencia= models.CharField(max_length=200)

#       def __str__(self):
#          return self
from django.db import models
 # Create your models here.
class Producto(models.Model):
     nombre = models.CharField(max_length=200)
     categorias  = models.CharField(max_length=200)
     detalles  = models.CharField(max_length=200)
     precios  = models.CharField(max_length=200)
    #  referencia= models.ForeignKey(Carrito, on_delete=models.CASCADE)

     def __str___(self):
         return self.nombre
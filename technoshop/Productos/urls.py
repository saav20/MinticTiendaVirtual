from django.urls import path
from Productos import views



urlpatterns = [
    path("",views.ListProductosAPIView.as_view(),name="Productos_list"),
    path("create/", views.CreateProductosAPIView.as_view(),name="Productos_create"),
    path("update/<int:pk>/",views.UpdateProductosAPIView.as_view(),name="update_Productos"),
    path("delete/<int:pk>/",views.DeleteProductosAPIView.as_view(),name="delete_Productos")
]
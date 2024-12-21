from django.urls import path
from Apps.warehouses.warehouse import views

urlpatterns = [
    
    path('shelves/', views.shelf_list, ),
    path('shelves/create/', views.shelf_create),
    path('registry/', views.warehouse_products)
]
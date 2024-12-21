from django.contrib import admin
from WareHouse.models import Product, Shelf, Warehouse 
# Register your models here.
admin.site.register(Warehouse)
admin.site.register(Shelf)
admin.site.register(Product)
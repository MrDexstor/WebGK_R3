from WareHouse.models import Product
from ServerAPI.items import item__info

def syncGlobalStock(request, warehouse_id):
    products = Product.objects.filter(warehouse=warehouse_id)

    for product in products:
        plu = product.plu
        item_info = item__info(request, plu)

        if item_info:
            product.name = item_info.get('fullName', product.name)
            product.global_stock = item_info.get('stock', -9999)
        else:
            product.global_stock = -9999

        product.save()

6
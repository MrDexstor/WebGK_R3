from django.shortcuts import  get_object_or_404, redirect
from django.http import JsonResponse
from WareHouse.models import Shelf, Product
from django.views.decorators.csrf import csrf_exempt
import json
from ServerAPI.items import item__info


# Удаление товара
@csrf_exempt
def delete_product(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        product.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

# Изменение количества товара
@csrf_exempt
def update_product_quantity(request, product_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        quantity = data.get('quantity')
        print(f'Quantity is at HTML : {data}')
        product = get_object_or_404(Product, id=product_id)
        product.stock_on_shelf = quantity
        product.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

# Перемещение товара
@csrf_exempt
def move_product(request, product_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        quantity = int(data.get('quantity'))
        destination = data.get('destination')
        product = get_object_or_404(Product, id=product_id)

        if destination == 'sale':
            if quantity == product.stock_on_shelf:
                product.delete()
            else:
                product.stock_on_shelf -= quantity
                product.save()
        else:
            destination_shelf = get_object_or_404(Shelf, id=destination)
            if quantity == product.stock_on_shelf:
                product.delete()
            else:
                product.stock_on_shelf -= quantity
                product.save()

            existing_product = Product.objects.filter(plu=product.plu, shelf=destination_shelf).first()
            if existing_product:
                existing_product.stock_on_shelf += quantity
                existing_product.save()
            else:
                Product.objects.create(plu=product.plu, name=product.name, stock_on_shelf=quantity, global_stock=product.global_stock, shelf=destination_shelf, warehouse=destination_shelf.warehouse)

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

# Добавление товара
@csrf_exempt
def add_product(request, shelf_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        barcode = data.get('barcode')
        quantity = data.get('quantity')
        item = item__info(request, barcode)

        if item == {}:
            return JsonResponse({'status': 'error', 'message': 'Товар не найден'}, status=400)

        shelf = get_object_or_404(Shelf, id=shelf_id)
        existing_product = Product.objects.filter(plu=item['article'], shelf=shelf).first()

        if existing_product:
            existing_product.stock_on_shelf += int(quantity)
            existing_product.save()
        else:
            Product.objects.create(plu=item['article'], name=item['fullName'], stock_on_shelf=quantity, global_stock=item['stock'], shelf=shelf, warehouse=shelf.warehouse)

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

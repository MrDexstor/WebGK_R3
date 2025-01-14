import json
from Lib.UI import render, redirect, Page
from ServerAPI import items


'''
def item_info(request, plu):
    item = items.item__info(request, plu)
    page = Page('Информация о товаре WebGK', 'Информация о товаре', item['article'])
    page.returnUrl(request.META.get('HTTP_REFERER'))
    return render(request, page, 'dm_style/items/item_info.html', {"item": item})
   
   
def item_movements(request, plu):
    item = items.item__movements(request, plu)
    return render(request, 'items/item_movements.html', 'Информация о товаре', {"item": item})


def item_plg(request, plu):
    item = items.item__plg(request, plu)
    return render(request, 'items/item_plg.html', 'Информация о товаре', {"item": item})


def item_datamatrix(request, plu):
    item = items.item__info(request, plu)
    
    return render(request, 'items/item_datamatrix.html', 'Честный знак. Маркировка', {"item": item})
'''
def search(request):
    if request.method == 'POST':
        article = request.POST.get('plu', None)
        nameContains = request.POST.get('item_name', None)
        limit = request.POST.get('max-position', None)
        # Запросить из системы данные 
        sr_result = items.search(request, itemIds= article, nameContains=nameContains, limit = limit)
        if len(sr_result) == 1:
            return redirect(f'/GK/items/item/{ sr_result[0]['article'] }/info')
        elif len(sr_result) == 0:
            return redirect('/GK/items/')
        else: 
            page = Page('Поиск товара', 'Поиск товара', 'Найдены товары по вашему запросу')
            page.returnUrl('/GK/items/')
            return render(request, page, 'dm_style/items/search_result.html', {'items': sr_result})
            
    else:
        page = Page('Поиск товара', 'Поиск товара', 'Диалог поиска товаров')
        page.returnUrl('/GK/')
        return render(request, page, 'products/item/search.html')
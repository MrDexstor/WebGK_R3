from django.urls import path, include
from Apps import root


urlpatterns = [
    # Дашбоард системы 
    path('', root.dashboard),
    # Меню
    path('menu/', include('Apps.menu.urls')),
    # Товарооборот и товары
    path('products/', include('Apps.products.urls')),
    # Сессии и пользователи
    path('session/', include('Apps.session.urls')),
]

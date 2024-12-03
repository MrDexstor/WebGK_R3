from django.urls import path, include
from Apps import root


urlpatterns = [
    # Дашбоард системы 
    path('', root.dashboard),
    # Меню
    path('menu/', include('Apps.menu.urls')),
]

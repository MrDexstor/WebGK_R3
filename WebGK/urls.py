from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('GK/', include('Apps.urls')),
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import path, include
from Lib.UI import redirect

def main(request):
    return redirect('/GK/')
    
    
urlpatterns = [
    path('', main),
    path('GK/', include('Apps.urls')),
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import path, include
from SyncModule.sync import InitSync, receive_file

urlpatterns = [
    path('syncInit/', InitSync),
    path('accept_file/', receive_file)
    ]

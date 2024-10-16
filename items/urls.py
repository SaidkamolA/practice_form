from django.contrib import admin
from django.urls import path, include

from items.views import *

urlpatterns = [
    path('index/', index, name='index'),
    path('dob/', dobavlenie, name='dobavlenie'),
    path('dob2/', create, name='create'),
    path('udalenie/<int:id>', udalenie, name='udalenie'),
    path('izm/<int:id>', izmen, name='izmen'),
    path('items/<int:pk>', get_item, name='get_item'),
    path('str/', str, name='str'),
]

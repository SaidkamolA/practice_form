from dataclasses import fields

from django.contrib import admin
from django.contrib.admin import ModelAdmin

from items.models import *


# Register your models here.


class ItemAdmin(ModelAdmin):
    list_display = ['id', 'name', 'description', 'price']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Item, ItemAdmin)


class CategoryAdmin(ModelAdmin):
    list_display = ['id', 'name']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


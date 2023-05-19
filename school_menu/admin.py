from django.contrib import admin
from .models import Menu, MenuItems

class MenuItemsInline(admin.TabularInline):
    model = MenuItems

@admin.register(Menu)
class PartnersAdmin(admin.ModelAdmin):
    inlines = [MenuItemsInline, ]
    list_display = ['school', 'title']

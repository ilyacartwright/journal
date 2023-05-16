from django.contrib import admin
from .models import Employees, PlaceWork, Cabinet, Classes, Items, Groups

class AdminPlaceWork(admin.TabularInline):
    model = PlaceWork

@admin.register(Employees)
class AdminEmpluyees(admin.ModelAdmin):
    inlines = [AdminPlaceWork,]
    list_display = ['last_name', 'first_name', 'surname']

@admin.register(Cabinet)
class AdminCabinet(admin.ModelAdmin):
    list_display = ['number', 'floor', 'name', 'employee']


class AdminGroups(admin.TabularInline):
    model = Groups

class AdminItems(admin.TabularInline):
    model = Items

@admin.register(Classes)
class AdminClasses(admin.ModelAdmin):
    inlines = [AdminGroups, AdminItems,]
    list_display = ['school', 'number']
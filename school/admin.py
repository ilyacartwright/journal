from django.contrib import admin
from .models import Employees, PlaceWork

class AdminPlaceWork(admin.TabularInline):
    model = PlaceWork

@admin.register(Employees)
class AdminEmpluyees(admin.ModelAdmin):
    inlines = [AdminPlaceWork,]
    list_display = ['last_name', 'first_name', 'surname']
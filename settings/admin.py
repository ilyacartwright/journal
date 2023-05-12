from django.contrib import admin
from .models import Schools, Positions


@admin.register(Schools)
class AdminSchools(admin.ModelAdmin):
    pass

@admin.register(Positions)
class AdminPositions(admin.ModelAdmin):
    pass
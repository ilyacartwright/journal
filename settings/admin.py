from django.contrib import admin
from .models import Schools, Positions, AcademicSubjects


@admin.register(Schools)
class AdminSchools(admin.ModelAdmin):
    pass


@admin.register(Positions)
class AdminPositions(admin.ModelAdmin):
    pass


@admin.register(AcademicSubjects)
class AdminAcademicSubjects(admin.ModelAdmin):
    pass

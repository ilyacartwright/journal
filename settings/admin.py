from django.contrib import admin
from .models import Schools


@admin.register(Schools)
class SchoolsInline(admin.ModelAdmin):
    pass
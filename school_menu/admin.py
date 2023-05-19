from django.contrib import admin
from .models import Partners, PartnersItems, Sites, SitesItems

class PartnersItemsInline(admin.TabularInline):
    model = PartnersItems

@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    inlines = [PartnersItemsInline, ]
    list_display = ['school']


class SitesItemsInline(admin.TabularInline):
    model = SitesItems

@admin.register(Sites)
class SitesAdmin(admin.ModelAdmin):
    inlines = [SitesItemsInline, ]
    list_display = ['school']
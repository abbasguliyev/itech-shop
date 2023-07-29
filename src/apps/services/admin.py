from django.contrib import admin
from apps.services.models import Services

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name',)
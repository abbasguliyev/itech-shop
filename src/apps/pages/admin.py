from django.contrib import admin
from apps.pages.models import Contact, Company, Partners

admin.site.site_header = 'ITECH SHOP Admin'
admin.site.site_title = 'adminsitration of ITech Shop'

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'phone', 'message')
    list_display_links = ('id', 'email')
    list_filter = ('email',)
    search_fields = ('email', 'first_name', 'last_name', 'phone', 'message')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone',)
    list_display_links = ('id', 'phone')

@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
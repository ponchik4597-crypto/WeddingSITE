from django.contrib import admin

from .models import Guest


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'presence', 'plusone', 'drink')
    list_filter = ('presence', 'plusone')
    search_fields = ('name',)
    list_per_page = 50

from django.contrib import admin

from pesquisa.models import Urna


@admin.register(Urna)
class UrnaAdmin(admin.ModelAdmin):
    list_display = list_display = ['id', 'serial']
    list_display_links = list_display
    list_filter = ['adesivo', 'horario']
    search_fields = ('serial',)
    list_per_page = 100

from django.contrib import admin

# Register your models here.
from commande.models import Commande


@admin.register(Commande)
class CommandesAdmin(admin.ModelAdmin):
    list_display = ('get_products','referanceCmd', 'dateCmd', 'get_products',)
    ordering = ('referanceCmd',)
    list_filter = ('referanceCmd',)
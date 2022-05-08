from django.contrib import admin

# Register your models here.
from produit.models import Produit


@admin.register(Produit)
class ProduitsAdmin(admin.ModelAdmin):
    list_display = ('produitRef', 'nomProduit', 'description', 'dateProduit', 'prix',)
    ordering = ('nomProduit',)
    list_filter = ('produitRef', 'nomProduit',)
    search_fields = ('produitRef', 'nomProduit',)
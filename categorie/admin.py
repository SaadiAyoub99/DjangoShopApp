from django.contrib import admin

# Register your models here.
from categorie.models import Categorie


@admin.register(Categorie)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('nomCategorie', )
    ordering = ('nomCategorie',)
    list_filter = ('nomCategorie', )
    search_fields = ('nomCategorie', )
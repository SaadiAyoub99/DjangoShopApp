from django.contrib import admin

# Register your models here.
from personne.models import Personne


@admin.register(Personne)
class PersonnesAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email',)
    ordering = ('prenom',)
    list_filter = ('nom', 'prenom',)
    search_fields = ('nom', 'prenom',)
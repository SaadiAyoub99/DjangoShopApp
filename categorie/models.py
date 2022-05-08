from django.db import models

# Create your models here.
class Categorie(models.Model):
    nomCategorie = models.CharField(max_length=50)

    class Meta:
        ordering = ['nomCategorie']

    def __str__(self):
        return self.nomCategorie
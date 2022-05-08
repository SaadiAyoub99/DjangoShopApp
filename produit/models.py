from django.db import models
from categorie.models import Categorie
# Create your models here.
class Produit(models.Model):
    produitRef = models.CharField(max_length=50)
    nomProduit = models.CharField(max_length=50)
    description = models.TextField(null=True)
    image = models.CharField(max_length=5000, null=True)
    dateProduit = models.DateField()
    prix = models.FloatField(max_length=50)
    Categorie = models.ForeignKey(
        Categorie,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['produitRef']

    def __str__(self):
        return self.nomProduit

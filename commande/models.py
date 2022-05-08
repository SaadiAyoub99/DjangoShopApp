from django.db import models

# Create your models here.
from personne.models import Personne
from produit.models import Produit

class Commande(models.Model):
    referanceCmd = models.CharField(max_length=50)
    dateCmd = models.DateField()
    produits = models.ManyToManyField(Produit)
    personne = models.ForeignKey(
        Personne,
        on_delete=models.CASCADE
    )
    def get_products(self):
        return "\n".join([p.produits for p in self.produit.all()])

    def get_products(self):
        return "".join([p.products for p in self.produits.all()])

    class Meta:
        ordering = ['referanceCmd']

    def __str__(self):
        return self.referanceCmd

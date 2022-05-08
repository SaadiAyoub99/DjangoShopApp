from django.db import models

# Create your models here.
class Personne(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)

    class Meta:
        ordering = ['email']

    def __str__(self):
        return self.email
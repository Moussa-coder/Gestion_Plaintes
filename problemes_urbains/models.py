from django.db import models
from django.contrib.auth.models import User

class Probleme(models.Model):
    CATEGORIES = (
        ('denis', 'Dénis'),
        ('routes', 'Routes endommagées'),
        ('eau', 'Coupures d\'eau'),
        ('eclairage', 'Éclairage public'),
        ('autre', 'Autre'),
    )

    titre = models.CharField(max_length=200)
    description = models.TextField()
    categorie = models.CharField(max_length=20, choices=CATEGORIES)
    localisation = models.CharField(max_length=255)
    date_creation = models.DateTimeField(auto_now_add=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    statut = models.CharField(max_length=20, default='nouveau') 
    photo = models.ImageField(upload_to='photos_problemes/', null=True, blank=True)



    def _str_(self):
        return self.titre
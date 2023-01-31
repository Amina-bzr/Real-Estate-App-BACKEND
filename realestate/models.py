from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Options du chanmp Categorie
vente = 'Vente'
echange = 'Echange'
location = 'Location'
location_vac = 'Location pour vacances'

choix_categorie = [
    (vente, 'Vente'),
    (echange, 'Échange'),
    (location, 'Location'),
    (location_vac, 'Location pour vacances'),
]

# {"categorie":"Vente", "type": "villa", "surface":12.000, "description":"hhh", "prix":123566, "wilaya":"alger","commune":"hydra","addresse":"jhjhkl12356"}


class Annonce(models.Model):
    # le champ id est generé automatiquement par Django
    categorie = models.CharField(
        max_length=25,
        choices=choix_categorie,
        default=vente,
    )
    type = models.CharField(max_length=30)
    surface = models.FloatField(max_length=30)
    description = models.TextField()
    prix = models.FloatField(max_length=30)
    utilisateur = models.ForeignKey(
        User, on_delete=models.CASCADE,)  # on tire d'ici le contact
    wilaya = models.CharField(max_length=25)
    commune = models.CharField(max_length=25)
    addresse = models.CharField(max_length=40)
    date_pub = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_pub']


class Photo(models.Model):  # table qui contient touttes les photos
    annonce = models.ForeignKey(
        Annonce, on_delete=models.CASCADE, related_name="photos")
    photo = models.ImageField(upload_to='annonces/', editable=True)


class Offre(models.Model):
    utilisateur = models.ForeignKey(
        User, on_delete=models.CASCADE)
    annonce = models.ForeignKey(
        Annonce, on_delete=models.CASCADE, related_name='offres')
    contenu = models.TextField()


class Contact(models.Model):
    # Email, prenom et nom sont dans "utilisateur"
    utilisateur = models.OneToOneField(
        User, on_delete=models.CASCADE)
    addresse = models.CharField(max_length=50)
    telephone = models.CharField(max_length=15)

from django.urls import reverse
from realestate.models import Annonce, Offre
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


# tests Annonce
class AnnonceTests(APITestCase):
    url = reverse('annonce-list')

    def setUp(self):
        self.user = User.objects.create_user(
            username='test', password='test')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    #test de la recuperation des annonces
    def test_get_annonces(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #test de la création d'une annonce
    def test_post_annonce(self):
        ancienne_taille = Annonce.objects.count()
        data = {"titre": "Belle villa à vendre",
                "Categorie": "Vente",
                "Type": "villa",
                "Surface": 150.0,
                "Description": "très belle villa avec piscine chauffée et une belle vue au calme absolu",
                "Prix": 4123566,
                "Wilaya": "Alger",
                "Commune": "Hydra",
                "Addresse": "Hydra, rue 16, Alger"}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ancienne_taille+1, Annonce.objects.count())


# tests Offre
class OffreTests(APITestCase):
    url = reverse('offre-list')

    def setUp(self):
        self.user = User.objects.create_user(
            username='test', password='test')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    #test de la recuperation des offres
    def test_get_Offres(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


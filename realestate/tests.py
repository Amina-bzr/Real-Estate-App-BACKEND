from django.urls import reverse
from realestate.models import Annonce, Offre
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
# selenium
from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

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

#test selenium
class OffreTests(APITestCase):
    url = reverse('offre-list')

    def setUp(self):
        self.user = User.objects.create_user(
            username='test', password='test')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    # test de la recuperation des offres
    def test_get_Offres(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class AnnonceFormTest(LiveServerTestCase):

    def testform(self):
        driver = webdriver.Chrome()
        driver.get("http://localhost:5173")
        main_page = driver.current_window_handle

        # selectionner le boutton du login
        time.sleep(5)
        btn_login = driver.find_element(By.ID, "googlesign")
        btn_login.click()

        # s'authentifier

        for handle in driver.window_handles:
            if handle != main_page:
                login_page = handle

        driver.switch_to.window(login_page)

        time.sleep(5)
        email_field = driver.find_element(By.ID, "identifierId")
        email_field.send_keys("trialcomptetrial@gmail.com")

        next_button = driver.find_element(By.ID, "identifierNext")
        next_button.click()
        time.sleep(3)
        password_field = driver.switch_to.active_element
        password_field.send_keys("appart1234")

        signin_button = driver.find_element(By.ID, "passwordNext")
        signin_button.click()

        #revenir à la fenetre principale
        time.sleep(2)
        driver.switch_to.window(main_page)
        
        
        # aller à la page "publier"
        time.sleep(5)

        publier_btn = driver.find_element(By.ID, "publier")
        publier_btn.click()


        #remplir le formulaire
        time.sleep(5)
        input_field = driver.find_element(By.ID, "titre")
        input_field.send_keys("nouvelle annonce")

        input_field1 = driver.find_element(By.ID, "Surface")
        input_field1.send_keys("2000")

        input_field2 = driver.find_element(By.ID, "Description")
        input_field2.send_keys("annonce pour vente d'une maison")

        input_field3 = driver.find_element(By.ID, "Commune")
        input_field3.send_keys("babezouar")

        input_field4 = driver.find_element(By.ID, "Prix")
        input_field4.send_keys("5000")

        input_field5 = driver.find_element(By.ID, "Addresse")
        input_field5.send_keys("street5")

        select_element = Select(driver.find_element(By.ID, "Categorie"))
        select_element.select_by_visible_text("Vente")

        select_element2 = Select(driver.find_element(By.ID, "Type"))
        select_element2.select_by_visible_text("Maison")

        select_element3 = Select(driver.find_element(By.ID, "Wilaya"))
        select_element3.select_by_visible_text("Alger")

        image_uploader = driver.find_element("name", "images")
        image_uploader.send_keys(
            "/home/amina/developement/api-realestate-app/media/userPhotos/profilePic.jpg")
        image_uploader.send_keys(
            "/home/amina/developement/api-realestate-app/media/userPhotos/profilePic1.jpg")

        button = driver.find_element(By.CLASS_NAME, "upload-btn")
        button.click()
        button2 = driver.find_element(By.ID, "pub")
        button2.click()

        driver.quit()

from django.urls import path
from realestate import views

urlpatterns = [
    path('annonces/', views.Annonce_list, name="annonce-list"),
    path('annonces/<int:pk>/', views.Annonce_detail, name="annonce-detail"),

    path('offres/', views.Offre_list, name="offre-list"),
    path('offres/<int:pk>/', views.Offre_detail, name="offre-detail"),

    path('contacts/', views.Contact_list, name="contact-list"),
    path('contacts/<int:pk>/', views.Contact_detail, name="contact-detail"),

    path('users/', views.User_list, name="user-list"),
    path('users/<int:pk>/', views.User_detail, name="user-detail"),

    path('groups/', views.Group_list, name="group-list"),
    path('groups/<int:pk>/', views.Group_detail, name="group-detail"),

    path('photos/', views.Photo_list, name="photo-list"),
    path('photos/<int:pk>/', views.Photo_detail, name="photo-detail"),

    path('token-auth/', views.Google_login, name="google-login")


]

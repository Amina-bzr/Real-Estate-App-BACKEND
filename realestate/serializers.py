from django.contrib.auth.models import User, Group
from .models import Annonce, Offre, Contact, Photo
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    contact = serializers.HyperlinkedRelatedField(
        view_name='contact-detail', read_only=True)

    class Meta:
        model = User
        fields = "__all__"


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class OffreSerializer(serializers.HyperlinkedModelSerializer):
    utilisateur = serializers.CharField(
        source='utilisateur.username', required=False)
    annonce = serializers.HyperlinkedRelatedField(
        view_name='annonce-detail', read_only=True)

    class Meta:
        model = Offre
        fields = "__all__"


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    utilisateur = serializers.CharField(
        source='utilisateur.username', required=False)

    class Meta:
        model = Contact
        fields = "__all__"


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    photo = serializers.ImageField()

    class Meta:
        model = Photo
        fields = "__all__"


class AnnonceSerializer(serializers.HyperlinkedModelSerializer):
    annonceur = serializers.CharField(
        source='annonceur.username', required=False)
    offres = serializers.HyperlinkedRelatedField(
        many=True, view_name="offre-detail", read_only=True)
    photos = serializers.HyperlinkedRelatedField(
        many=True, view_name='photo-detail', read_only=True)

    class Meta:
        model = Annonce
        fields = "__all__"

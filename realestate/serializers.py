from django.contrib.auth.models import User, Group
from .models import Annonce, Offre, Contact, Photo
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    contact = serializers.HyperlinkedRelatedField(
        view_name='offre-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'contact']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class OffreSerializer(serializers.HyperlinkedModelSerializer):
    utilisateur = serializers.ReadOnlyField(source='utilisateur.username')
    annonce = serializers.HyperlinkedRelatedField(
        view_name='annonce-detail', read_only=True)

    class Meta:
        model = Offre
        fields = "__all__"


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"


class AnnonceSerializer(serializers.HyperlinkedModelSerializer):
    ''' annonceur = serializers.ReadOnlyField(source='annonceur.username')
    offres = serializers.HyperlinkedRelatedField(
        many=True, view_name='offre-detail', read_only=True)
    photos = serializers.HyperlinkedRelatedField(
        many=True, view_name='photo-detail', read_only=True)
    offres = serializers.HyperlinkedRelatedField(
        many=True, view_name='offre-detail', read_only=True) '''

    offres = OffreSerializer(many=True, read_only=True)
    photos = PhotoSerializer(many=True)
    annonceur = UserSerializer(read_only=True)

    class Meta:
        model = Annonce
        fields = "__all__"

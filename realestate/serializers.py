from django.contrib.auth.models import User, Group
from .models import Annonce, Offre, Contact, Photo
from rest_framework import serializers
from rest_framework.response import Response


class ContactSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Contact
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    contact = ContactSerializer(many=False)
    id = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ['id', 'contact', 'username',
                  'first_name', 'last_name', 'email']

    def create(self, validated_data):
        Contact_data = validated_data.pop('contact')
        user = User.objects.create(**validated_data)
        Contact.objects.create(utilisateur=user, **Contact_data)
        return user

    def update(self, instance, validated_data):
        contact_data = validated_data.pop('contact')
        contact = instance.contact

        # mise à jour de l'utilisateur
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        # mise à jour du contact
        contact.telephone = contact_data.get(
            'telephone', contact.telephone)
        contact.addresse = contact_data.get('addresse', contact.addresse)
        contact.save()

        return instance


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class OffreSerializer(serializers.ModelSerializer):
    utilisateur = serializers.CharField(
        source='utilisateur.username', required=False)
    id = serializers.ReadOnlyField()

    class Meta:
        model = Offre
        fields = ["id", "annonce", "contenu", "utilisateur"]

    def create(self, validated_data):
        annonce_id = validated_data.pop('annonce')
        try:
            offre = Offre.objects.create(
                annonce=annonce_id, **validated_data)
        except Annonce.DoesNotExist:
            return Response("Annonce with given id doesn't exist", status=status.HTTP_400_BAD_REQUEST)

        return offre


class PhotoSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField()
    id = serializers.ReadOnlyField()

    class Meta:
        model = Photo
        fields = ["id", "annonce", "photo"]

    def create(self, validated_data):
        annonce_id = validated_data.pop('annonce')
        try:
            photo = Photo.objects.create(
                annonce=annonce_id, **validated_data)
        except Annonce.DoesNotExist:
            return Response("Annonce with given id doesn't exist", status=status.HTTP_400_BAD_REQUEST)

        return photo


class AnnonceSerializer(serializers.ModelSerializer):
    utilisateur = serializers.CharField(
        source='utilisateur.username', required=False)
    offres = OffreSerializer(many=True, read_only=True)
    photos = PhotoSerializer(many=True, read_only=True)
    id = serializers.ReadOnlyField()

    class Meta:
        model = Annonce
        fields = "__all__"

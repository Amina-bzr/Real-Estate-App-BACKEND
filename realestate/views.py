from gc import get_objects
from django.contrib.auth.models import User, Group

from .utils import post_object, put_object, get_objects, delete_object
from .models import Annonce, Offre, Photo, Contact
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, AnnonceSerializer, OffreSerializer, ContactSerializer, PhotoSerializer, GroupSerializer


''' class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class AnnonceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Annonce.objects.all()
    serializer_class = AnnonceSerializer
    permission_classes = [permissions.IsAuthenticated]


class OffreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Offre.objects.all()
    serializer_class = OffreSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]


class PhotoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticated] '''
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
# @authentication_classes(permissions.IsAuthenticatedOrReadOnly)
def Annonce_list(request):
    """
    recuperer la liste des annonces, ou ajouter une annonce.
    """

    if request.method == 'GET':
        return get_objects(request, AnnonceSerializer, Annonce)

    elif request.method == 'POST':
        return post_object(request, AnnonceSerializer)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def Annonce_detail(request, pk):
    """
    recuperer, modifier ou supprimer une annonce.
    """
    try:
        annonce = Annonce.objects.get(pk=pk)
    except Annonce.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AnnonceSerializer(annonce, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        return put_object(request, AnnonceSerializer, annonce)

    elif request.method == 'DELETE':
        return delete_object(request, annonce)


@ api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def Offre_list(request):
    """
    recuperer la liste des Offres, ou ajouter une Offre.
    """

    if request.method == 'GET':
        return get_objects(request, OffreSerializer, Offre)

    elif request.method == 'POST':
        return post_object(request, OffreSerializer)


@ api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def Offre_detail(request, pk):
    """
    recuperer, modifier ou supprimer une Offre.
    """
    try:
        offre = Offre.objects.get(pk=pk)
    except Offre.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OffreSerializer(offre, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        return put_object(request, OffreSerializer, offre)

    elif request.method == 'DELETE':
        return delete_object(request, offre)


@ api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def Photo_list(request):
    """
    recuperer la liste des Photos, ou ajouter une Photo.
    """

    if request.method == 'GET':
        return get_objects(request, PhotoSerializer, Photo)

    elif request.method == 'POST':
        return post_object(request, PhotoSerializer)


@ api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def Photo_detail(request, pk):
    """
    recuperer, modifier ou supprimer une Photo.
    """
    try:
        photo = Photo.objects.get(pk=pk)
    except Photo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PhotoSerializer(photo, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        return put_object(request, PhotoSerializer, photo)

    elif request.method == 'DELETE':
        return delete_object(request, photo)


@ api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def User_list(request):
    """
    recuperer la liste des Users, ou ajouter une User.
    """

    if request.method == 'GET':
        return get_objects(request, UserSerializer, User)

    elif request.method == 'POST':
        return post_object(request, UserSerializer)


@ api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def User_detail(request, pk):
    """
    recuperer, modifier ou supprimer une User.
    """
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        return put_object(request, UserSerializer, user)

    elif request.method == 'DELETE':
        return delete_object(request, user)


@ api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def Contact_list(request):
    """
    recuperer la liste des Contacts, ou ajouter une Contact.
    """

    if request.method == 'GET':
        return get_objects(request, ContactSerializer, Contact)

    elif request.method == 'POST':
        return post_object(request, ContactSerializer)


@ api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def Contact_detail(request, pk):
    """
    recuperer, modifier ou supprimer une Contact.
    """
    try:
        contact = Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ContactSerializer(contact, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        return put_object(request, ContactSerializer, contact)

    elif request.method == 'DELETE':
        return delete_object(request, contact)


@ api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def Group_list(request):
    """
    recuperer la liste des Groups, ou ajouter une Group.
    """

    if request.method == 'GET':
        return get_objects(request, GroupSerializer, Group)

    elif request.method == 'POST':
        return post_object(request, GroupSerializer)


@ api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def Group_detail(request, pk):
    """
    recuperer, modifier ou supprimer une Group.
    """
    try:
        group = Group.objects.get(pk=pk)
    except Group.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GroupSerializer(group, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        return put_object(request, GroupSerializer, group)

    elif request.method == 'DELETE':
        return delete_object(request, group)

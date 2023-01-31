from django.http import JsonResponse
from django.utils.crypto import get_random_string
from rest_framework import authentication
from django.contrib.auth.models import User
from gc import get_objects
from django.contrib.auth.models import User, Group
from rest_framework.authtoken.models import Token
from .utils import post_object, put_object, get_objects, delete_object, get_annonces, get_users
from .models import Annonce, Offre, Photo, Contact
from .serializers import UserSerializer, AnnonceSerializer, OffreSerializer, ContactSerializer, PhotoSerializer, GroupSerializer
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
        return get_annonces(request, AnnonceSerializer, Annonce)

    elif request.method == 'POST':
        return post_object(request, AnnonceSerializer, 'utilisateur')


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
        return post_object(request, OffreSerializer, 'utilisateur')


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
# @permission_classes([IsAuthenticated])
def User_list(request):
    """
    recuperer la liste des Users, ou ajouter une User.
    """

    if request.method == 'GET':
        return get_users(request, UserSerializer, User)

    elif request.method == 'POST':
        return post_object(request, UserSerializer, None)


@ api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
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


@ api_view(['POST'])
def Google_login(request):
    try:
        user = User.objects.get(email=request.data['email'])
        token = Token.objects.get(user=user).key
    except User.DoesNotExist:
        # create user
        username = request.data['name']
        email = request.data['email']
        given_name = request.data['given_name']
        family_name = request.data['family_name']
        user = User.objects.create_user(
            username=username, email=email, first_name=given_name, last_name=family_name)
        token = Token.objects.create(user=user).key
        # send token
    return JsonResponse({'token': token})


@ api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def Contact_list(request):
    """
    recuperer la liste des Contacts, ou ajouter un Contact.
    """

    if request.method == 'GET':
        return get_objects(request, ContactSerializer, Contact)

    elif request.method == 'POST':
        return post_object(request, ContactSerializer, 'utilisateur')


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


# may be deleted later
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

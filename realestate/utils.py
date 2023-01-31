from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .filters import AnnonceFilter, UserFilter
from django_filters.utils import translate_validation


def put_object(request, serializer, object):
    if request.user == (object or object.utilisateur or object.annonce.utilisateur):
        serializer = serializer(object, data=request.data, partial=True,
                                context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)


def post_object(request, serializer, utilisateur):

    serializer = serializer(data=request.data, context={'request': request})
    print(request.data)
    if serializer.is_valid():

        if utilisateur != None:
            # dans le case de annonce, offre et contact (on retire l'utilisateur qui a creé l'objet depuis l'objet request)
            serializer.save(utilisateur=request.user)

        else:
            serializer.save()  # pour Photo pas d'attribut utilisateur associé

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# traitement particulier (filtrage)
def get_annonces(request, serializer, model):
    annonces = model.objects.all()
    filterset = AnnonceFilter(request.GET, queryset=annonces)
    if not filterset.is_valid():
        raise translate_validation(filterset.errors)
    serializer = serializer(filterset.qs, many=True,
                            context={'request': request})
    return Response(serializer.data)


# traitement particulier (filtrage+perms(à confirmer))
def get_users(request, serializer, model):
    users = model.objects.all()
    filterset = UserFilter(request.GET, queryset=users)
    if not filterset.is_valid():
        raise translate_validation(filterset.errors)
    serializer = serializer(filterset.qs, many=True,
                            context={'request': request})
    return Response(serializer.data)


def get_objects(request, serializer, model):
    objects = model.objects.all()
    serializer = serializer(objects, many=True, context={'request': request})
    return Response(serializer.data)


def delete_object(request, object):
    if request.user == (object.utilisateur or object.annonce.utilisateur) or request.user.is_superuser:
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_403_FORBIDDEN)

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


def put_object(request, serializer, object):
    if request.user == object.annonceur:
        serializer = serializer(object, data=request.data,
                                context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)


def post_object(request, serializer):

    serializer = serializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save(annonceur=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_objects(request, serializer, model):
    annonces = model.objects.all()
    serializer = serializer(annonces, many=True, context={'request': request})
    return Response(serializer.data)


def delete_object(request, object):
    if request.user == (object.annonceur or object.annonce.annonceur or object.utilisateur):
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_403_FORBIDDEN)

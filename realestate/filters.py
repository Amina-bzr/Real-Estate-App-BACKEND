from .models import Annonce
from django.contrib.auth.models import User
from django_filters import rest_framework


class AnnonceFilter(rest_framework.FilterSet):
    min_date = rest_framework.DateFilter(
        field_name="date_pub", lookup_expr='gte')
    max_date = rest_framework.DateFilter(
        field_name="date_pub", lookup_expr='lte')

    class Meta:
        model = Annonce
        fields = ['type', 'wilaya', 'commune']


class UserFilter(rest_framework.FilterSet):

    class Meta:
        model = User
        fields = ['username', 'email']

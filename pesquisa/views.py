from django.db import models
from pesquisa.models import Urna
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters

from pesquisa.serializers import UrnaSerializer


class UrnaFilter(filters.FilterSet):
    class Meta:
        model = Urna
        fields = ['serial', 'adesivo']


class UrnaViewSet(ModelViewSet):
    queryset = Urna.objects.all()
    serializer_class = UrnaSerializer

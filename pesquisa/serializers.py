from django.db import models
from django.db.models import fields
from rest_framework import serializers

from pesquisa.models import Urna


class UrnaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Urna
        fields = ['serial', 'linha', 'horario', 'adesivo']

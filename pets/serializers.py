from dataclasses import fields
from rest_framework import serializers
from .models import Pets

class PetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pets
        fields = ("id", "nome", "historia", "foto")
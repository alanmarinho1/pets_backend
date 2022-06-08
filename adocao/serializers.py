from dataclasses import fields
import imp
from rest_framework import serializers
from .models import Adocao

from pets.serializers import PetsSerializer
from pets.models import Pets


class AdocaoSerializer(serializers.ModelSerializer):
    pets = PetsSerializer(many=False, read_only=True)
    pets_id = serializers.PrimaryKeyRelatedField(
        many=False, write_only=True, queryset=Pets.objects.all()
    )

    class Meta:
        model = Adocao
        fields = ("id", "valor", "email", "pets", "pets_id")

    def create(self, validated_data):
        validated_data["pets"] = validated_data.pop("pets_id")
        return super().create(validated_data)

    def validate_valor(self, value):
        if value < 10:
            raise serializers.ValidationError("Deve ser maior que 10")
        if value > 100:
            raise serializers.ValidationError("Deve ser menor que 100")
        return value

from unicodedata import decimal
from django.db import models


class Adocao(models.Model):
    valor = models.DecimalField(blank=False, null=False, max_digits=5, decimal_places=2)
    email = models.EmailField(null=False, blank=False, max_length=255)
    pets = models.ForeignKey(to="pets.Pets", null=False, on_delete=models.CASCADE)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from .models import Pets
from .serializers import PetsSerializer

class PetsList(APIView):
    def get(self, request, format=None):
        pets = Pets.objects.all()
        serializer = PetsSerializer(pets, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
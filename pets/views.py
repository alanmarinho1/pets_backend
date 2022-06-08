from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from .models import Pets
from .serializers import PetsSerializer


class PetsList(APIView):
    def get(self, request, format=None):
        pets = Pets.objects.all()
        serializer = PetsSerializer(pets, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    def post(self, request, format=None):
        serializer = PetsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(
            {
                "message": "Houveram erros de validação",
                "errors": serializer.errors
            },
            status=HTTP_400_BAD_REQUEST,
        )

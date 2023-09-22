from rest_framework import viewsets, mixins
from rest_framework import permissions
from .models import Anuncio
from .serializers import AnuncioSerializer


class AnuncioViewSet(
        viewsets.GenericViewSet,
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.ListModelMixin
    ):
    """
    Endpoint que permite ações CRUD com Anúncios, com exceção do método DELETE
    """

    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer
    permission_classes = [permissions.AllowAny]

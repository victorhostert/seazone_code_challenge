from rest_framework import viewsets, mixins
from rest_framework import permissions
from .models import Reserva
from .serializers import ReservaSerializer


class ReservaViewSet(
        viewsets.GenericViewSet,
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.DestroyModelMixin,
        mixins.ListModelMixin
    ):
    """
    Endpoint que permite ações CRUD com Imóveis, com exceção do método UPDATE
    """

    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    permission_classes = [permissions.AllowAny]

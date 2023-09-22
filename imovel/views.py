from rest_framework import viewsets
from rest_framework import permissions
from .models import Imovel
from .serializers import ImovelSerializer


class ImovelViewSet(viewsets.ModelViewSet):
    """
    Endpoint que permite ações CRUD com Imóveis
    """

    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer
    permission_classes = [permissions.AllowAny]


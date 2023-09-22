from django.urls import include, path
from rest_framework import routers
from anuncio.views import AnuncioViewSet
from imovel.views import ImovelViewSet
from reserva.views import ReservaViewSet


router = routers.DefaultRouter()
router.register(r'anuncio', AnuncioViewSet, basename='anuncio')
router.register(r'imovel', ImovelViewSet, basename='imovel')
router.register(r'reserva', ReservaViewSet, basename='reserva')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
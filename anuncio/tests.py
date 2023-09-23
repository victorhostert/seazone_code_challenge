from rest_framework.test import APITestCase
from rest_framework import status
from anuncio.models import Anuncio
from imovel.models import Imovel

class AnuncioTestCase(APITestCase):
    def setUp(self):
        imoveis = Imovel.objects.all()
        Anuncio.objects.bulk_create(
            [
                Anuncio(imovel=imoveis[0], plataforma_nome="AirBnB", plataforma_taxa=0.10),
                Anuncio(imovel=imoveis[1], plataforma_nome="Booking", plataforma_taxa=0.15),
                Anuncio(imovel=imoveis[2], plataforma_nome="TripAdvisor", plataforma_taxa=0.20),
            ]
        )

    def test_anuncio_criado_corretamente(self):
        """Verifica se o setUp criou os anúncios"""
        response = self.client.get(
            '/api/v1/anuncio/'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        anuncio_pk = Anuncio.objects.first().pk
        response = self.client.get(
            f'/api/v1/anuncio/{anuncio_pk}/'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_criar_anuncio_novo(self):
        """Verifica a possibilidade de criar novos anúncios"""
        response = self.client.post(
            '/api/v1/anuncio/',
            {
                'imovel': 1,
                'plataforma_nome': 'Teste',
                'plataforma_taxa': 0.15,
            } 
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_atualizacao_anuncio(self):
        """Verifica se é possível atualizar um anúncio"""
        anuncio_pk = Anuncio.objects.first().pk
        response = self.client.patch(
            f'/api/v1/anuncio/{anuncio_pk}/',
            {
                'plataforma_nome': 'Teste'
            }
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_deletar_anuncio(self):
        """Verifica se é possível deletar um anúncio(Não deve ser possível)"""
        anuncio_pk = Anuncio.objects.first().pk
        response = self.client.delete(
            f'/api/v1/anuncio/{anuncio_pk}/'
        )
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
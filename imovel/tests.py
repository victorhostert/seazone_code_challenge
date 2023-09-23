from rest_framework.test import APITestCase
from rest_framework import status
from imovel.models import Imovel


class ImovelTestCase(APITestCase):
    def setUp(self):
        Imovel.objects.bulk_create(
            [
                Imovel(
                    limite=3,
                    qntd_banheiro=2,
                    animais=True,
                    valor_limpeza=150.00,
                    data_ativacao='2023-04-15',
                ),
                Imovel(
                    limite=4,
                    qntd_banheiro=1,
                    animais=False,
                    valor_limpeza=170.50,
                    data_ativacao='2023-06-25',
                )
            ]
        )

    def test_imovel_criado_corretamente(self):
        """Verifica se o setUp criou os imóveis"""
        response = self.client.get(
            '/api/v1/imovel/'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        imovel_pk = Imovel.objects.first().pk
        response = self.client.get(
            f'/api/v1/imovel/{imovel_pk}/'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_criar_imovel_novo(self):
        """Verifica a possibilidade de criar novos imóveis"""
        response = self.client.post(
            '/api/v1/imovel/',
            {
                'limite': 2,
                'qntd_banheiro': 1,
                'animais': True,
                'valor_limpeza': 100.00,
                'data_ativacao': '2023-09-11'
            }
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_atualizacao_imovel(self):
        """Verifica se é possível atualizar um imóvel"""
        imovel_pk = Imovel.objects.first().pk
        response = self.client.patch(
            f'/api/v1/imovel/{imovel_pk}/',
            {
                'limite': 10
            }
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_deletar_imovel(self):
        """Verifica se é possível deletar um imóvel"""
        imovel_pk = Imovel.objects.first().pk
        response = self.client.delete(
            f'/api/v1/imovel/{imovel_pk}/'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
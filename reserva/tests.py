from rest_framework.test import APITestCase
from rest_framework import status
from anuncio.models import Anuncio
from reserva.models import Reserva

class AnuncioTestCase(APITestCase):
    def setUp(self):
        anuncios = Anuncio.objects.all()
        Reserva.objects.bulk_create(
            [
                Reserva(
                    anuncio=anuncios[0],
                    check_in='2023-08-20',
                    check_out='2023-09-01',
                    preco=700.00,
                    comentario='Lorem ipsum dolor sit amet',
                ),
                Reserva(
                    anuncio=anuncios[1],
                    check_in='2023-08-15',
                    check_out='2023-09-23',
                    preco=145.50,
                    comentario='Quisque nec turpis neque. Ut porta magna nec mauris vehicula, mattis luctus libero sollicitudin',
                ),
                Reserva(
                    anuncio=anuncios[2],
                    check_in='2023-05-20',
                    check_out='2023-05-22',
                    preco=300.00,
                    comentario='',
                )
            ]
        )

    def test_reserva_criado_corretamente(self):
        """Verifica se o setUp criou as reservas"""
        response = self.client.get(
            '/api/v1/reserva/'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        reserva_pk = Reserva.objects.first().pk
        response = self.client.get(
            f'/api/v1/reserva/{reserva_pk}/'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_criar_reserva_com_data_check_in_errada(self):
        """Verifica se é possível criar uma data check_in posterior a data de check-out"""
        response = self.client.post(
            '/api/v1/reserva/', 
            {
                'anuncio': 1,
                'check_in': '2023-01-02',
                'check_out': '2023-01-01',
                'preco': 100.00,
                'comentario': '', 
            }
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_criar_reserva_novo(self):
        """Verifica a possibilidade de criar novas reservas"""
        response = self.client.post(
            '/api/v1/reserva/',
            {
                'anuncio': 1,
                'check_in': '2023-01-02',
                'check_out': '2023-01-03',
                'preco': 100.00,
                'comentario': '', 
            }
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_atualizacao_reserva(self):
        """Verifica se é possível atualizar uma reserva (Não deve ser possível)"""
        response = self.client.patch(
            f'/api/v1/reserva/{Reserva.objects.first().pk}/',
            {
                'comentario': 'Teste'
            }
        )
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        
    def test_deletar_reserva(self):
        """Verifica se é possível deletar uma reserva"""
        response = self.client.delete(f'/api/v1/reserva/{Reserva.objects.first().pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
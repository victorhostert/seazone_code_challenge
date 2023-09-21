from django.db import models
from imovel.models import Imovel


class Anuncio(models.Model):
    imovel = models.ForeignKey(
        verbose_name='Imóvel',
        to=Imovel,
        on_delete=models.CASCADE,
    )
    plataforma_nome = models.CharField(
        verbose_name='Nome da Plataforma',
        max_length=255,
    )
    plataforma_taxa = models.DecimalField(
        verbose_name='Taxa da Plataforma',
        decimal_places=2,
        max_digits=10,
    )
    data_hora_criacao = models.DateTimeField(
        verbose_name='Data e Hora de Criação',
        auto_now_add=True,
        null=False,
        blank=False,
    )
    data_hora_atualizacao = models.DateTimeField(
        verbose_name='Data e Hora da Última Atualização',
        auto_now=True,
    )
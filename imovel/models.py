from django.db import models


class Imovel(models.Model):
    codigo = models.AutoField(
        verbose_name='Código do Imóvel',
        auto_created=True,
        unique=True,
        primary_key=True,
        editable=False,
    )
    limite = models.IntegerField(
        verbose_name='Limite de Hóspedes',
    )
    qntd_banheiro = models.IntegerField(
        verbose_name='Quantidade de banheiros',
    )
    animais = models.BooleanField(
        verbose_name='Permissão para Animais de Estimação',
        default=False,
    )
    valor_limpeza = models.DecimalField(
        verbose_name='Valor para Limpeza',
        decimal_places=2,
        max_digits=10,
    )
    data_ativacao = models.DateField(
        verbose_name='Data de Ativação',
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
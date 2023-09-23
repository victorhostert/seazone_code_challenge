from django.db import models
from anuncio.models import Anuncio
import uuid


class Reserva(models.Model):
    codigo = models.UUIDField(
        verbose_name='Código da Reserva',
        primary_key=True,
        default = uuid.uuid4,
        editable = False,
    )
    anuncio = models.ForeignKey(
        verbose_name='Anúncio',
        to=Anuncio,
        on_delete=models.CASCADE,
    )
    check_in = models.DateField(
        verbose_name='Data de Check-in'
    )
    check_out = models.DateField(
        verbose_name='Data de Check-out'
    )
    preco = models.DecimalField(
        verbose_name='Preço Total',
        decimal_places=2,
        max_digits=10,
    )
    comentario = models.TextField(
        verbose_name='Comentário',
        null=True,
        blank=True
    )
    
    def __str__(self) -> str:
        return f'Reserva {self.codigo} - Anúncio: {self.anuncio}'

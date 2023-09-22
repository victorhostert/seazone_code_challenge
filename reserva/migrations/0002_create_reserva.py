# Generated by Django 4.2.5 on 2023-09-22 21:27

from django.db import migrations

class Migration(migrations.Migration):
    def create_reserva(apps, schema_editor):
        """Cria 8 reservas"""
        Anuncio = apps.get_model("anuncio", "Anuncio")
        anuncios = Anuncio.objects.all()
        Reserva = apps.get_model("reserva", "Reserva")
        db_alias = schema_editor.connection.alias
        Reserva.objects.using(db_alias).bulk_create(
            [
                Reserva(
                    anuncio=anuncios[0],
                    check_in='2023-08-20',
                    check_out='2023-09-01',
                    preco=700.00,
                    comentario='Lorem ipsum dolor sit amet',
                ),
                Reserva(
                    anuncio=anuncios[0],
                    check_in='2023-08-15',
                    check_out='2023-09-23',
                    preco=145.50,
                    comentario='Quisque nec turpis neque. Ut porta magna nec mauris vehicula, mattis luctus libero sollicitudin',
                ),
                Reserva(
                    anuncio=anuncios[1],
                    check_in='2023-05-20',
                    check_out='2023-05-22',
                    preco=300.00,
                    comentario='',
                ),
                Reserva(
                    anuncio=anuncios[1],
                    check_in='2023-08-21',
                    check_out='2023-08-24',
                    preco=450.95,
                    comentario='Praesent sit amet pellentesque urna. Quisque lorem velit, placerat quis lorem quis, interdum bibendum sapien. Proin vitae pulvinar massa.',
                ),
                Reserva(
                    anuncio=anuncios[1],
                    check_in='2023-08-11',
                    check_out='2024-09-01',
                    preco=1000.00,
                    comentario='Lorem ipsum dolor sit amet',
                ),
                Reserva(
                    anuncio=anuncios[2],
                    check_in='2023-08-20',
                    check_out='2023-09-10',
                    preco=800.00,
                    comentario='Nullam massa justo, scelerisque vitae condimentum vitae, bibendum vitae ligula. Pellentesque sit amet iaculis ante. Morbi eleifend sagittis purus',
                ),
                Reserva(
                    anuncio=anuncios[2],
                    check_in='2023-08-01',
                    check_out='2023-09-28',
                    preco=2000.00,
                    comentario='Lorem ipsum dolor sit amet',
                ),
                Reserva(
                    anuncio=anuncios[2],
                    check_in='2023-08-20',
                    check_out='2023-09-01',
                    preco=300.00,
                    comentario='Lorem ipsum dolor sit amet',
                ),
            ]
        )

    dependencies = [
        ('reserva', '0001_initial'),
        ('anuncio', '0002_create_anuncio')
    ]

    operations = [
        migrations.RunPython(create_reserva)
    ]
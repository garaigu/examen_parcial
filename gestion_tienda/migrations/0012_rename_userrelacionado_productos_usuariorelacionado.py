# Generated by Django 4.1.7 on 2023-04-15 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_tienda', '0011_alter_productos_preciocompra_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productos',
            old_name='userRelacionado',
            new_name='usuarioRelacionado',
        ),
    ]

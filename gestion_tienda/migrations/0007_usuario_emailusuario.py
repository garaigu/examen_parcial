# Generated by Django 4.1.7 on 2023-04-14 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_tienda', '0006_remove_usuario_emailusuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='emailUsuario',
            field=models.CharField(default='', max_length=32),
        ),
    ]

# Generated by Django 4.1.7 on 2023-04-13 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_tienda', '0003_remove_usuario_perfilusuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='tipoUsuario',
            field=models.CharField(default='VENDEDOR', max_length=32),
        ),
    ]

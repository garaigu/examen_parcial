# Generated by Django 4.1.7 on 2023-04-14 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_tienda', '0007_usuario_emailusuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='emailUsuario',
            field=models.CharField(default='mogugaai1399@gmail.com', max_length=32),
        ),
    ]

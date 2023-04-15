from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipoUsuario = models.CharField(max_length=32, default='VENDEDOR')
    nroCelular = models.CharField(max_length=9, default='999888777')
    fechaIngreso = models.DateField(default=date.today)
    
class Productos(models.Model):
    usuarioRelacionado = models.ForeignKey(User, on_delete=models.CASCADE)
    nombreProducto = models.CharField(max_length=32, default='')
    codigoProducto = models.CharField(max_length=8, default='COD-0000')
    precioCompra = models.DecimalField(max_digits=4, default=1.00, decimal_places=2)
    precioVenta = models.DecimalField(max_digits=4, default=1.00, decimal_places=2)

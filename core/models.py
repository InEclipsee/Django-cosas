from django.db import models

# Create your models here.
class Residencia (models.Model):
    id = models.IntegerField(primary_key=True)
    dueno = models.CharField(max_length=50)
    telefono = models.CharField(max_length=12)
    correo = models.CharField(max_length=50)

class Correspondencia (models.Model):
    fechaRecepcion = models.DateField()
    conserje = models.CharField(max_length=50)
    remitente = models.CharField(max_length=50)
    destinatario = models.CharField(max_length=50)
    estado = [
        ('R', 'Recibido'),
        ('EC', 'En camino'),
        ('RET', 'Retenido'),
        ('AD', 'En aduana'),
        ('COR', 'En sede de correo')]
    idResidencia = models.ForeignKey(Residencia, on_delete=models.CASCADE)

from django.db import models
from django.utils import timezone

class Genero(models.Model):
    genero = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.genero
    
    class meta:
        db_table = 'Genero'
    
class Ocupacion(models.Model):
    ocupacion = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.ocupacion
    
    class meta:
        db_table = 'Ocupacion'

class EstadoCivil(models.Model):
    estadoCivil= models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.estadoCivil
    
    class meta:
        db_table = 'EstadoCivil'

class Estado(models.Model):
    estado = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.estado
    
    class meta:
        db_table = 'Estado'

class Ciudad(models.Model):
    ciudad = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.ciudad
    
    class meta:
        db_table = 'Ciudad'

class Profile(models.Model):
    nombre = models.CharField(max_length=254, null=False)
    apellidoPaterno = models.CharField(max_length=254, null=False)
    apellidoMaterno = models.CharField(max_length=254, null=False)
    edad = models.IntegerField(null=False)
    ciudad = models.CharField(max_length=254, null=False)
    genero = models.CharField(max_length=254, null=False)
    ocupacion = models.CharField(max_length=254, null=False)
    estado = models.CharField(max_length=254, null=False)
    estadoCivil = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
    
    class meta:
        db_table = 'Profile'

# Create your models here.


# Create your models here.

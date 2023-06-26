from django.db import models

# Create your models here.
class TblMovilidad(models.Model):
    movilidad_id = models.AutoField(primary_key=True)
    movilidad_tipo_servicio = models.CharField(max_length=45)
    movilidad_turno = models.CharField(max_length=45)
    movilidad_seccion = models.CharField(max_length=45)
    movilidad_docente = models.CharField(max_length=255)
    movilidad_pago = models.FloatField()
    
    
    

class TblMovilidadRuta(models.Model):
    movilidad_ruta_id = models.AutoField(primary_key=True)
    movilidad_ruta_direccion = models.CharField(max_length=255)
    movilidad_ruta_hora_recojo = models.TimeField(blank=True, null=True)
    movilidad_ruta_hora_retorno = models.TimeField(blank=True, null=True)
    movilidad = models.ForeignKey(TblMovilidad, models.DO_NOTHING)
    
    
    def __str__(self) -> str:
        return self.movilidad_ruta_direccion

from django.db import models

# Create your models here.

class GuiaRemision(models.Model):
    punto_par = models.CharField(max_length=50)
    punto_lle = models.CharField(max_length=50)
    fecha_traslado = models.DateField()
    costo_min = models.IntegerField()
    nom_empresa_transportes = models.CharField(max_length=100)
    ruc_empresa_transportes = models.CharField(max_length=50)
    marca_num_placa = models.CharField(max_length=50)
    nro_cons_inscripcion = models.CharField(max_length=50)
    nro_lic_conductor = models.CharField(max_length=50)
    tipo_num_comp_pago = models.CharField(max_length=50)
    orden_compra = models.CharField(max_length=50)
    cliente = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'guia_remision'
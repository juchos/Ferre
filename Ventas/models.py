from django.db import models

# Create your models here.

class Ventas(models.Model):
    no_facturas = models.IntegerField(db_column='No_Facturas')  # Field name made lowercase.
    productos = models.IntegerField(db_column='Productos')  # Field name made lowercase.
    cantidad = models.IntegerField()
    importe = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ventas'
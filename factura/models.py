from django.db import models

# Create your models here.

class Factura(models.Model):
    no_facturas = models.IntegerField(db_column='No_Facturas')  # Field name made lowercase.
    cliente = models.IntegerField()
    fecha = models.DateField()
    totals = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'facturas'
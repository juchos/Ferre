# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Productos(models.Model):
    nombreproductos = models.CharField(db_column='nombreProductos', max_length=45)  # Field name made lowercase.
    preciosproductos = models.FloatField(db_column='preciosProductos')  # Field name made lowercase.
    descripcionproductos = models.CharField(db_column='descripcionProductos', max_length=200)  # Field name made lowercase.
    cantidadproductos = models.IntegerField(db_column='cantidadProductos')  # Field name made lowercase.
    preciocompraproductos = models.FloatField(db_column='preciocompraProductos')  # Field name made lowercase.
    difererencia = models.FloatField(db_column='Difererencia')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productos'

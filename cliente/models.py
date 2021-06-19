# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cliente(models.Model):
    nombre_cliente = models.CharField(db_column='Nombre_Cliente', max_length=45)  # Field name made lowercase.
    apellido_cliente = models.CharField(db_column='Apellido_Cliente', max_length=45)  # Field name made lowercase.
    razon_s_cliente = models.CharField(db_column='razon_s_Cliente', max_length=200)  # Field name made lowercase.
    ruc_cliente = models.CharField(db_column='ruc_Cliente', max_length=20)  # Field name made lowercase.
    direccion_cliente = models.CharField(db_column='direccion_Cliente', max_length=100)  # Field name made lowercase.
    telefono_cliente = models.CharField(db_column='telefono_Cliente', max_length=20)  # Field name made lowercase.
    correo_cliente = models.CharField(db_column='correo_Cliente', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cliente'



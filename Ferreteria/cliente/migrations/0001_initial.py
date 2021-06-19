# Generated by Django 3.2.4 on 2021-06-19 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idcliente', models.IntegerField(db_column='idCliente')),
                ('nombre_cliente', models.CharField(db_column='Nombre_Cliente', max_length=45)),
                ('apellido_cliente', models.CharField(db_column='Apellido_Cliente', max_length=45)),
                ('razon_s_cliente', models.CharField(db_column='razon_s_Cliente', max_length=200)),
                ('ruc_cliente', models.CharField(db_column='ruc_Cliente', max_length=20)),
                ('direccion_cliente', models.CharField(db_column='direccion_Cliente', max_length=100)),
                ('telefono_cliente', models.CharField(db_column='telefono_Cliente', max_length=20)),
                ('correo_cliente', models.CharField(db_column='correo_Cliente', max_length=50)),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
    ]
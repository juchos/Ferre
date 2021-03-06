# Generated by Django 3.2.4 on 2021-06-19 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idproductos', models.IntegerField(db_column='idProductos')),
                ('nombreproductos', models.CharField(db_column='nombreProductos', max_length=45)),
                ('preciosproductos', models.FloatField(db_column='preciosProductos')),
                ('descripcionproductos', models.CharField(db_column='descripcionProductos', max_length=200)),
                ('cantidadproductos', models.IntegerField(db_column='cantidadProductos')),
                ('preciocompraproductos', models.FloatField(db_column='preciocompraProductos')),
                ('difererencia', models.FloatField(db_column='Difererencia')),
            ],
            options={
                'db_table': 'productos',
                'managed': False,
            },
        ),
    ]

# Generated by Django 3.2.4 on 2021-06-19 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idventas', models.IntegerField(db_column='idVentas')),
                ('no_facturas', models.IntegerField(db_column='No_Facturas')),
                ('productos', models.IntegerField(db_column='Productos')),
                ('cantidad', models.IntegerField()),
                ('importe', models.IntegerField()),
            ],
            options={
                'db_table': 'ventas',
                'managed': False,
            },
        ),
    ]

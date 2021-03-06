# Generated by Django 2.1.7 on 2019-02-18 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mproduct_id', models.IntegerField()),
                ('mproduct_name', models.CharField(max_length=50)),
                ('mproduct_cost', models.IntegerField()),
                ('mproduct_color', models.CharField(max_length=50)),
                ('mproduct_class', models.CharField(max_length=10)),
                ('mnumber_of_products', models.IntegerField()),
                ('mcustomer_name', models.CharField(max_length=50)),
                ('mmobile_number', models.BigIntegerField()),
                ('memail', models.EmailField(max_length=50)),
            ],
        ),
    ]

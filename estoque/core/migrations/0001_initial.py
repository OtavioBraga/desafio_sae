# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 19:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome do produto')),
                ('average_coast', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Preço médio')),
                ('quantity', models.IntegerField(default=0, verbose_name='Quantidade')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor da total da compra')),
                ('quantity', models.IntegerField(default=1, verbose_name='Quantidade')),
                ('purchase_date', models.DateField(default=django.utils.timezone.now, verbose_name='Data da compra')),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Product')),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
                'ordering': ['-purchase_date'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=120, verbose_name='Task Id')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]

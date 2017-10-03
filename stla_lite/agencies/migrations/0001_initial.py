# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-03 17:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('agency_name', models.CharField(max_length=100, verbose_name='Agency Name')),
                ('agency_acronym', models.CharField(max_length=10, verbose_name='Agency Acronym')),
                ('agency_code', models.IntegerField(primary_key=True, serialize=False, verbose_name='Agency Code')),
            ],
        ),
        migrations.CreateModel(
            name='CostCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost_center_name', models.CharField(max_length=40, verbose_name='Cost Center Name')),
                ('cost_center_code', models.IntegerField(verbose_name='Cost Center Code')),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agencies.Agency')),
            ],
        ),
    ]
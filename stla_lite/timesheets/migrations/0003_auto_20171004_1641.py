# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-04 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheets', '0002_auto_20171003_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_category',
            field=models.CharField(choices=[('X', 'Regular Time'), ('V', 'Vacation'), ('S', 'Sick'), ('P', 'Personal'), ('B', 'Bereavement'), ('H', 'Holiday'), ('J', 'Jury Duty'), ('W', 'Workers Compensation'), ('UB', 'Union Duties'), ('training_conf_sem', 'Training, Conference, or Seminar'), ('other', 'Other')], default='X', max_length=30, verbose_name='Activity Category'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-04 20:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agencies', '0001_initial'),
        ('grants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grantaward',
            name='agency_code',
            field=models.ForeignKey(default=68, on_delete=django.db.models.deletion.CASCADE, to='agencies.Agency', verbose_name='Agency to which this grant corresponds.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grantawardtask',
            name='percent_allotted',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=5, verbose_name='What percentage of this task is taken up with existing allotments.'),
        ),
    ]

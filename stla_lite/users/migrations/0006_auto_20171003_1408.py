# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-03 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_email_max_length'),
        ('socialaccount', '0003_extra_data_default_dict'),
        ('timesheets', '0002_auto_20171003_1408'),
        ('admin', '0002_logentry_remove_auto_add'),
        ('users', '0005_auto_20171003_1321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hr',
            name='employee_ptr',
        ),
        migrations.RemoveField(
            model_name='supervisor',
            name='employee_ptr',
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Employee', 'verbose_name_plural': 'Employees'},
        ),
        migrations.RemoveField(
            model_name='employee',
            name='supervisor_id',
        ),
        migrations.AddField(
            model_name='employee',
            name='is_hr_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='is_supervisor',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='HR',
        ),
        migrations.DeleteModel(
            name='Supervisor',
        ),
    ]

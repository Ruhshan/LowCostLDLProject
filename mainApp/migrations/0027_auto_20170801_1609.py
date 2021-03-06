# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-01 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0026_auto_20170801_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='qc',
            name='level_1_lower_range',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='qc',
            name='level_1_upper_range',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='qc',
            name='level_2_lower_range',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='qc',
            name='level_2_upper_range',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='qc',
            name='level_3_lower_range',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='qc',
            name='level_3_upper_range',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

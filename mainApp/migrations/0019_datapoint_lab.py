# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 13:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0018_auto_20170617_0411'),
    ]

    operations = [
        migrations.AddField(
            model_name='datapoint',
            name='lab',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.Lab'),
        ),
    ]

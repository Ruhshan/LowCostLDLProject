# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 16:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0010_auto_20170610_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='lab',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.Lab'),
        ),
    ]

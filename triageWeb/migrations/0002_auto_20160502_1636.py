# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triageWeb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='latitude',
            field=models.DecimalField(decimal_places=8, default=0.0, max_digits=50),
        ),
        migrations.AddField(
            model_name='person',
            name='longitude',
            field=models.DecimalField(decimal_places=8, default=0.0, max_digits=50),
        ),
    ]
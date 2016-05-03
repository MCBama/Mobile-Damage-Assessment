# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 22:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triageWeb', '0011_auto_20160502_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='latitude',
            field=models.DecimalField(decimal_places=15, default=0.0, max_digits=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='longitude',
            field=models.DecimalField(decimal_places=15, default=0.0, max_digits=50),
        ),
    ]

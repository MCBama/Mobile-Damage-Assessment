# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 22:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('triageWeb', '0010_auto_20160502_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='updater',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='triageWeb.Reporter'),
        ),
    ]
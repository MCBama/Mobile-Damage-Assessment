# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 13:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('triageWeb', '0020_auto_20160503_0844'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='triage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='triageWeb.TriageArea'),
        ),
    ]
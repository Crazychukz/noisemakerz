# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-14 20:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('influencers', '0005_auto_20161113_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payouts',
            name='amount_requested',
            field=models.FloatField(default=0.0),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-03-07 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0039_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='variantpaper',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-04-11 07:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0011_auto_20170410_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='variant',
            name='BX_ID_1000_Genomes',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='variant',
            name='BX_ID_BIC',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='variant',
            name='BX_ID_ClinVar',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='variant',
            name='BX_ID_ENIGMA',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='variant',
            name='BX_ID_ESP',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='variant',
            name='BX_ID_ExAC',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='variant',
            name='BX_ID_LOVD',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='variant',
            name='BX_ID_exLOVD',
            field=models.TextField(default=b''),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-07 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0011_change_type_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datarelease',
            name='columns_added',
        ),
        migrations.RemoveField(
            model_name='datarelease',
            name='columns_deleted',
        ),
        migrations.RemoveField(
            model_name='datarelease',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='datarelease',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='datarelease',
            name='variants_added',
        ),
        migrations.RemoveField(
            model_name='datarelease',
            name='variants_deleted',
        ),
        migrations.RemoveField(
            model_name='datarelease',
            name='variants_modified',
        ),
        migrations.AddField(
            model_name='datarelease',
            name='data_link',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datarelease',
            name='data_schema',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datarelease',
            name='date_released',
            field=models.DateTimeField(),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datarelease',
            name='md5sum',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datarelease',
            name='release_notes',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
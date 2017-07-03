# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-02 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0009_auto_20170702_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegrambot',
            name='is_public',
            field=models.BooleanField(default=False, help_text='Note That, other user can modify/delete this configuration.'),
        ),
    ]
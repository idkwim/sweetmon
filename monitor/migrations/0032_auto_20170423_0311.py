# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 18:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0031_auto_20170423_0305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='email_alert',
            new_name='use_email_alert',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='is_encrypt',
            new_name='use_encryption',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='telegram_alert',
            new_name='use_telegram_alert',
        ),
    ]
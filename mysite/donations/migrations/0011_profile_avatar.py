# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0010_card_card_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='/static/donations/images/anonymous.png', upload_to=b''),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-08 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_auto_20170507_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='check',
            name='last_ping_body',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]

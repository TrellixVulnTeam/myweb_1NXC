# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-02-26 13:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usercourse',
            options={'verbose_name': '用户课程', 'verbose_name_plural': '用户课程'},
        ),
    ]

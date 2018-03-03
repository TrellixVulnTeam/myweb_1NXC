# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-02-27 00:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_course_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher_tell',
            field=models.CharField(default='', max_length=300, verbose_name='老师告诉你'),
        ),
        migrations.AddField(
            model_name='course',
            name='youneedknow',
            field=models.CharField(default='', max_length=300, verbose_name='课程须知'),
        ),
    ]

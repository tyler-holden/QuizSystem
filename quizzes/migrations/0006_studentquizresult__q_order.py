# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-10 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0005_auto_20170810_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentquizresult',
            name='_q_order',
            field=models.TextField(default=''),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 01:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0007_auto_20170329_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

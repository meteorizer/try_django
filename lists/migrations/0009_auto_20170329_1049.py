# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 01:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0008_auto_20170329_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='list',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='lists.List'),
        ),
    ]

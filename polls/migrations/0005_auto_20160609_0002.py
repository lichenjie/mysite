# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20160603_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trade',
            name='id',
        ),
        migrations.AlterField(
            model_name='trade',
            name='bankid',
            field=models.CharField(primary_key=True, max_length=200, serialize=False),
        ),
        migrations.AlterField(
            model_name='trade',
            name='mktcode',
            field=models.CharField(primary_key=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='trade',
            name='tradecode',
            field=models.CharField(primary_key=True, max_length=200),
        ),
    ]

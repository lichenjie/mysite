# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20160609_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='bankid',
            field=models.CharField(primary_key=True, max_length=200),
        ),
    ]

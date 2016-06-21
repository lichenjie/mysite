# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_trade'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='marketserial',
            field=models.CharField(default=datetime.datetime(2016, 6, 2, 14, 44, 34, 418291, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trade',
            name='mktcode',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]

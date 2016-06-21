# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20160602_1444'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trade',
            old_name='trade',
            new_name='tradecode',
        ),
    ]

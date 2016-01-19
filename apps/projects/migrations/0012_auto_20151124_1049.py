# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_auto_20151123_1640'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workitem',
            old_name='tag',
            new_name='tags',
        ),
    ]

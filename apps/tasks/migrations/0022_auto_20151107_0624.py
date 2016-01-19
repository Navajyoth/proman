# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0021_auto_20151106_1247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='sub_task',
            new_name='items',
        ),
    ]

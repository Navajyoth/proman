# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_workitem_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workitem',
            name='status',
            field=model_utils.fields.StatusField(default=b'added', max_length=100, no_check_for_status=True, choices=[(0, 'dummy')]),
        ),
    ]

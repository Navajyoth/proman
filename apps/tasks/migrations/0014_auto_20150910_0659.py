# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0013_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(max_length=2048, null=True, blank=True),
        ),
    ]

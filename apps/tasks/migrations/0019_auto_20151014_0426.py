# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0018_task_due_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='technology',
        ),
        migrations.RemoveField(
            model_name='task',
            name='work_type',
        ),
    ]

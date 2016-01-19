# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_auto_20151127_1501'),
        ('tasks', '0024_task_commits'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='workitem',
            field=models.ForeignKey(related_name='tasks', blank=True, to='projects.WorkItem', null=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_auto_20151124_0606'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='workitem',
            name='milestone',
            field=models.ForeignKey(related_name='workitems', blank=True, to='projects.Milestone', null=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0015_task_reviewer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='reviewer',
            field=models.ForeignKey(related_name='reviews', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]

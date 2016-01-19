# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_project_slack_channel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='slack_channel',
        ),
        migrations.RemoveField(
            model_name='project',
            name='slack_url',
        ),
    ]

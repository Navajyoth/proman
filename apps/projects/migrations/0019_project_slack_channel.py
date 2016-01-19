# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slack_channel',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
    ]

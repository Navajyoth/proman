# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_auto_20151130_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slack_url',
            field=models.URLField(max_length=512, null=True, blank=True),
        ),
    ]

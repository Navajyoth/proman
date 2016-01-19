# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20151123_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tag',
            field=jsonfield.fields.JSONField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='workitem',
            name='tag',
            field=jsonfield.fields.JSONField(null=True, blank=True),
        ),
    ]

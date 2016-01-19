# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0023_auto_20151125_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='commits',
            field=jsonfield.fields.JSONField(null=True, blank=True),
        ),
    ]

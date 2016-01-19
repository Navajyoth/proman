# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0018_pettytask'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='sub_task',
            field=jsonfield.fields.JSONField(null=True, blank=True),
        ),
    ]

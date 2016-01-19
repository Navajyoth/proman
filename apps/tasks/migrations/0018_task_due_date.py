# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0017_auto_20151007_0446'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]

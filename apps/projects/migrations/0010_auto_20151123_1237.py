# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_milestone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectwork',
            name='work_type',
        ),
        migrations.DeleteModel(
            name='ProjectWork',
        ),
    ]

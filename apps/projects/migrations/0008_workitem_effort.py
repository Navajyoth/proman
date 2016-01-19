# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_workitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='workitem',
            name='effort',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20150907_0858'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='slack_id',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
    ]

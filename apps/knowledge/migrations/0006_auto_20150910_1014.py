# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge', '0005_auto_20150910_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
    ]

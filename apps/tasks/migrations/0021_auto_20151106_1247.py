# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0020_merge'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ('due_date',)},
        ),
        migrations.AlterField(
            model_name='pettytask',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]

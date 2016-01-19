# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20151124_1049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='tag',
            new_name='tags',
        ),
    ]

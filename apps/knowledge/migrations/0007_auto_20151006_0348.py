# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge', '0006_auto_20150910_1014'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-pk',)},
        ),
    ]

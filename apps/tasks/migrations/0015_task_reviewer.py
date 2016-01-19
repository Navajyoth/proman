# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0014_auto_20150910_0659'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='reviewer',
            field=models.ForeignKey(related_name='reviews', default=10, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

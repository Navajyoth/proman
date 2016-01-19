# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('knowledge', '0003_auto_20150909_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(related_name='articles', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]

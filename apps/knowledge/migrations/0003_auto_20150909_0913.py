# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge', '0002_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image_url',
            field=models.URLField(max_length=256, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='short_description',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
    ]

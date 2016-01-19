# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(max_length=512, null=True, blank=True)),
                ('username', models.CharField(max_length=512, null=True, blank=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('comment', models.CharField(max_length=512, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Commit',
                'verbose_name_plural': 'Commits',
            },
        ),
    ]

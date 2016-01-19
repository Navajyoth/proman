# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0020_auto_20151212_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlackSetting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('channel', models.CharField(max_length=64, null=True, blank=True)),
                ('url', models.URLField(max_length=512, null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('notify_task', models.BooleanField()),
                ('notify_workitem', models.BooleanField()),
                ('project', models.ForeignKey(related_name='slack_settings', to='projects.Project')),
            ],
        ),
    ]

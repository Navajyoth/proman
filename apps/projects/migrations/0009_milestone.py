# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_workitem_effort'),
    ]

    operations = [
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('start_date', models.DateTimeField(null=True, blank=True)),
                ('end_date', models.DateTimeField(null=True, blank=True)),
                ('is_deleted', models.BooleanField(default=True)),
                ('project', models.ForeignKey(related_name='milestones', to='projects.Project')),
            ],
        ),
    ]

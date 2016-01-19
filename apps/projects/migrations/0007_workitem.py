# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20150907_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=512)),
                ('description', models.CharField(max_length=2048, null=True, blank=True)),
                ('project', models.ForeignKey(related_name='workitems', to='projects.Project')),
                ('workitem', models.ForeignKey(related_name='subitems', blank=True, to='projects.WorkItem', null=True)),
            ],
        ),
    ]

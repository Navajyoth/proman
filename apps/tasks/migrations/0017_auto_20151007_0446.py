# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0016_auto_20150914_0428'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubTask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=512)),
                ('is_completed', models.BooleanField(default=False)),
                ('kind', model_utils.fields.StatusField(default=b'task', max_length=100, no_check_for_status=True, choices=[(b'task', b'task'), (b'review', b'review'), (b'blog', b'blog')])),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(related_name='sub_tasks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='created_by',
            field=models.ForeignKey(related_name='created_tasks', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subtask',
            name='task',
            field=models.ForeignKey(related_name='sub_tasks', to='tasks.Task'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0017_auto_20151007_0446'),
    ]

    operations = [
        migrations.CreateModel(
            name='PettyTask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('modified_on', models.DateField(auto_now=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('effort', models.DecimalField(null=True, max_digits=3, decimal_places=1, blank=True)),
                ('user', models.ForeignKey(related_name='petty_task', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('user', 'id'),
            },
        ),
    ]

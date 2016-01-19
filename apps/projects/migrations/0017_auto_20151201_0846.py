# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def update_workitem_status(apps, schema_editor):
   Workitem = apps.get_model("projects", "Workitem")
   for item in Workitem.objects.all():
       item.status = 'added'
       item.save()


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_auto_20151130_1657'),
    ]

    operations = [
        migrations.RunPython(update_workitem_status),
    ]

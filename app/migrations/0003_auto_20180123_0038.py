# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180123_0038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='tesk',
            new_name='task',
        ),
    ]

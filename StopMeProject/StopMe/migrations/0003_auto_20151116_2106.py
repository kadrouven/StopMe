# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StopMe', '0002_auto_20151116_2103'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stations',
            new_name='Stations2',
        ),
    ]

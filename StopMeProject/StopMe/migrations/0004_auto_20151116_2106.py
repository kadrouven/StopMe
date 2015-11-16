# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StopMe', '0003_auto_20151116_2106'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stations2',
            new_name='Stations',
        ),
    ]

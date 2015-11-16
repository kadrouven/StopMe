# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StopMe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stationName', models.CharField(unique=True, max_length=128)),
                ('lat', models.CharField(max_length=128)),
                ('lng', models.CharField(max_length=128)),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]

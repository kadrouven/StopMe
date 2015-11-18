# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StopMe', '0004_auto_20151116_2106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('origin', models.CharField(max_length=128)),
                ('destination', models.CharField(max_length=128)),
                ('via', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='RouteStations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('routeID', models.ForeignKey(to='StopMe.Route')),
            ],
        ),
        migrations.RenameModel(
            old_name='Stations',
            new_name='Station',
        ),
        migrations.AddField(
            model_name='routestations',
            name='stationID',
            field=models.ForeignKey(to='StopMe.Station'),
        ),
    ]

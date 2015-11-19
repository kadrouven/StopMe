# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serviceNumber', models.CharField(max_length=10, null=True, blank=True)),
                ('origin', models.CharField(max_length=128)),
                ('destination', models.CharField(max_length=128)),
                ('via', models.CharField(max_length=128, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='RouteStations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('routeID', models.ForeignKey(to='StopMe.Route')),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stationName', models.CharField(unique=True, max_length=128)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('transtype', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='routestations',
            name='stationID',
            field=models.ForeignKey(to='StopMe.Station'),
        ),
    ]

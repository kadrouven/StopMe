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
            ],
        ),
        migrations.CreateModel(
            name='RouteStation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('route', models.ForeignKey(to='StopMe.Route')),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stationName', models.CharField(unique=True, max_length=128)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('type', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='routestation',
            name='station',
            field=models.ForeignKey(to='StopMe.Station'),
        ),
        migrations.AddField(
            model_name='route',
            name='destination',
            field=models.ForeignKey(related_name='destination', to='StopMe.Station'),
        ),
        migrations.AddField(
            model_name='route',
            name='origin',
            field=models.ForeignKey(related_name='origin', to='StopMe.Station'),
        ),
        migrations.AddField(
            model_name='route',
            name='via',
            field=models.ForeignKey(related_name='via', to='StopMe.Station'),
        ),
    ]

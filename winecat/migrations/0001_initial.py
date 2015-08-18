# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasting',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('vineyard', models.CharField(max_length=200)),
                ('varietal', models.CharField(max_length=200)),
                ('vintage', models.CharField(max_length=10)),
                ('acquisition_date', models.DateTimeField(verbose_name='date acquired')),
            ],
        ),
        migrations.AddField(
            model_name='tasting',
            name='wine',
            field=models.ForeignKey(to='winecat.Wine'),
        ),
    ]

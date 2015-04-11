# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_auto_20150407_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='prototype',
            name='course',
            field=models.CharField(default=None, max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='prototype',
            name='cover',
            field=models.ImageField(default=None, upload_to=b'BookExchange/', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prototype',
            name='faculty',
            field=models.CharField(default=None, max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='prototype',
            name='isbn13',
            field=models.IntegerField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='prototype',
            name='programme',
            field=models.CharField(default=None, max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='usedbooks',
            name='date',
            field=models.DateField(default=datetime.date.today),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='seller',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]

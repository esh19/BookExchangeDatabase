# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_auto_20150411_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prototype',
            name='course',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='prototype',
            name='faculty',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='prototype',
            name='isbn13',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='prototype',
            name='programme',
            field=models.CharField(max_length=100),
        ),
    ]

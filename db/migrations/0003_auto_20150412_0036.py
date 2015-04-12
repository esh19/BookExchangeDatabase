# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_auto_20150411_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prototype',
            name='isbn',
            field=models.CharField(serialize=False, primary_key=True, max_length=100),
            preserve_default=True,
        ),
    ]

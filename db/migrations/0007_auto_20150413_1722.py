# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0006_auto_20150412_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usedbooks',
            name='date',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
    ]

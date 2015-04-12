# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_auto_20150412_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prototype',
            name='edition',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prototype',
            name='newPrice',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prototype',
            name='year',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]

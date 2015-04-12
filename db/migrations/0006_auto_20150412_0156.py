# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0005_auto_20150412_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prototype',
            name='bookAuthor',
            field=models.CharField(max_length=100, null=True, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prototype',
            name='bookName',
            field=models.CharField(max_length=100, null=True, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prototype',
            name='course',
            field=models.CharField(max_length=100, null=True, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prototype',
            name='cover',
            field=models.CharField(max_length=100, null=True, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prototype',
            name='faculty',
            field=models.CharField(max_length=100, null=True, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prototype',
            name='programme',
            field=models.CharField(max_length=100, null=True, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prototype',
            name='publisher',
            field=models.CharField(max_length=100, null=True, default=''),
            preserve_default=True,
        ),
    ]

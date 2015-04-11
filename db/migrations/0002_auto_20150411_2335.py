# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usedbooks',
            old_name='isbn',
            new_name='prototype',
        ),
        migrations.RenameField(
            model_name='usedbooks',
            old_name='idSeller',
            new_name='seller',
        ),
        migrations.AddField(
            model_name='prototype',
            name='course',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='prototype',
            name='cover',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='prototype',
            name='faculty',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='prototype',
            name='programme',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='usedbooks',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='prototype',
            name='bookAuthor',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='prototype',
            name='bookName',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='prototype',
            name='publisher',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='seller',
            name='email',
            field=models.EmailField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='seller',
            name='sellerName',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='usedbooks',
            name='condition',
            field=models.CharField(default='', max_length=100),
        ),
    ]

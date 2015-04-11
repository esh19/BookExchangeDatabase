# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    replaces = [(b'db', '0001_initial'), (b'db', '0002_auto_20150407_2023'), (b'db', '0003_auto_20150411_1720'), (b'db', '0004_auto_20150411_1721')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prototype',
            fields=[
                ('isbn', models.IntegerField(serialize=False, primary_key=True)),
                ('bookName', models.CharField(max_length=100)),
                ('newPrice', models.IntegerField()),
                ('publisher', models.CharField(max_length=100)),
                ('bookAuthor', models.CharField(max_length=100)),
                ('edition', models.IntegerField()),
                ('year', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sellerName', models.CharField(max_length=100)),
                ('phoneNumber', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UsedBooks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.IntegerField()),
                ('condition', models.CharField(max_length=100)),
                ('seller', models.ForeignKey(to='db.Seller')),
                ('prototype', models.ForeignKey(to='db.Prototype')),
                ('date', models.DateField(default=datetime.date.today)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='prototype',
            name='course',
            field=models.CharField(max_length=100),
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
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='prototype',
            name='isbn13',
            field=models.IntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='prototype',
            name='programme',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='seller',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prototype',
            fields=[
                ('isbn', models.IntegerField(primary_key=True, serialize=False)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('price', models.IntegerField()),
                ('condition', models.CharField(max_length=100)),
                ('idSeller', models.ForeignKey(to='db.Seller')),
                ('isbn', models.ForeignKey(to='db.Prototype')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100)),
                ('author', models.CharField(unique=True, max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name=b'Date Published')),
                ('category', models.CharField(max_length=100)),
                ('hero_image', models.ImageField(upload_to=b'images/', verbose_name=b'Hero Image')),
                ('additional_image', models.ImageField(upload_to=b'images/', verbose_name=b'Additional Image')),
                ('body', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

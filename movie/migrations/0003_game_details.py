# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-17 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_movie_details_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('release_date', models.CharField(max_length=50)),
                ('video_link', models.CharField(max_length=1000)),
                ('banner', models.CharField(default='#', max_length=1000)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-19 01:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gadi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('gadicompanyname', models.CharField(max_length=30)),
                ('gadiname', models.CharField(max_length=30)),
                ('gadino', models.CharField(max_length=30)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0006_auto_20170724_2101'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_time', models.DateTimeField(auto_now=True)),
                ('blog_name', models.CharField(max_length=50)),
                ('blog_context', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=50)),
                ('blog_id', models.IntegerField(default=50)),
            ],
        ),
    ]
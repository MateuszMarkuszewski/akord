# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-17 16:44
from __future__ import unicode_literals

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('akord', '0007_auto_20170817_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wideo',
            name='url',
            field=embed_video.fields.EmbedVideoField(null=True),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-21 14:16
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('GroupsApp', '0005_remove_comment_cid'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='cid',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True),
        ),
    ]

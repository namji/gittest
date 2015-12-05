# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='reviews',
        ),
        migrations.AddField(
            model_name='review',
            name='restaurant',
            field=models.ForeignKey(null=True, to='restaurants.Restaurant'),
        ),
    ]

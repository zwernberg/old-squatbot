# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 10, 9, 1, 30, 5, 374484, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activity',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 10, 9, 1, 30, 10, 702407, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workout',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 10, 9, 1, 30, 18, 163017, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workout',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 10, 9, 1, 30, 25, 855383, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0003_auto_20151104_2009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='set',
            name='owner',
        ),
    ]

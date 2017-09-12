# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20170705_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='locations',
            field=models.CharField(blank=True, max_length=120, default='My Location Default', null=True),
        ),
    ]

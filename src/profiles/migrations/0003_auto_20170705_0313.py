# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profiles_locations'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='job',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='description',
            field=models.TextField(default='Please Enter The User Description Here'),
        ),
    ]

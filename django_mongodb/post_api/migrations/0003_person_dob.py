# Generated by Django 3.2.9 on 2022-12-09 14:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_api', '0002_remove_person_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='dob',
            field=models.DateField(blank=None, default=datetime.datetime(2022, 12, 9, 20, 24, 9, 741091), null=None),
        ),
    ]

# Generated by Django 3.2.9 on 2022-12-09 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='dob',
        ),
    ]
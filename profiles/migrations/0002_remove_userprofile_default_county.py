# Generated by Django 3.1.3 on 2020-11-26 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='default_county',
        ),
    ]
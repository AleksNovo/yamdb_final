# Generated by Django 2.2.16 on 2022-11-29 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='confirmation_code',
        ),
    ]

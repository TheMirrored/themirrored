# Generated by Django 4.2.5 on 2023-11-05 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='downloadresourcesform',
            name='year',
        ),
    ]

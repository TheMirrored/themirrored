# Generated by Django 4.2.5 on 2023-10-10 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailusers', '0013_userprofile_bio_userprofile_facebook_url_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='facebook_url',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='instagram_url',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='linkedin_url',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='threads_url',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='twitter_url',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='youtube_url',
        ),
    ]
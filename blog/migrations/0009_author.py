# Generated by Django 4.2.5 on 2023-11-03 15:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0008_ipmodel_blogpage_likes_blogpage_views_howpage_likes_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('bio', models.TextField(blank=True, null=True)),
                ('facebook_url', models.URLField(blank=True, max_length=500, null=True)),
                ('twitter_url', models.URLField(blank=True, max_length=500, null=True)),
                ('instagram_url', models.URLField(blank=True, max_length=500, null=True)),
                ('threads_url', models.URLField(blank=True, max_length=500, null=True)),
                ('linkedin_url', models.URLField(blank=True, max_length=500, null=True)),
                ('youtube_url', models.URLField(blank=True, max_length=500, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Author profile',
                'verbose_name_plural': 'Author profiles',
            },
        ),
    ]

# Generated by Django 4.2.5 on 2023-11-05 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0009_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='siteemails',
            options={'verbose_name_plural': 'Site Emails'},
        ),
        migrations.RemoveField(
            model_name='author',
            name='id',
        ),
        migrations.AddField(
            model_name='author',
            name='page_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogpage',
            name='post_author',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='howpage',
            name='how_author',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='how_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='weeklywordpage',
            name='word_author',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='word_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='author',
            name='user',
            field=models.OneToOneField(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
    ]

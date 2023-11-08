# Generated by Django 4.2.5 on 2023-11-05 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_remove_author_last_login_remove_author_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='post_author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_author', to='blog.author'),
        ),
        migrations.AlterField(
            model_name='howpage',
            name='how_author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='how_author', to='blog.author'),
        ),
        migrations.AlterField(
            model_name='weeklywordpage',
            name='word_author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='word_author', to='blog.author'),
        ),
    ]
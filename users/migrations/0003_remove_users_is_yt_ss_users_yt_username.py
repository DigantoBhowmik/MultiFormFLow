# Generated by Django 4.1.13 on 2024-01-22 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_is_insta_ss_users_is_instra_ss_users_yt_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='is_yt_ss',
        ),
        migrations.AddField(
            model_name='users',
            name='yt_username',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
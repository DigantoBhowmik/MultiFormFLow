# Generated by Django 4.1.13 on 2024-01-22 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_users_is_yt_ss_users_yt_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='instra_username',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]

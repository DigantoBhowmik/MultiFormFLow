# Generated by Django 4.1.13 on 2024-01-21 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='is_insta_ss',
            new_name='is_instra_ss',
        ),
        migrations.AddField(
            model_name='users',
            name='yt_url',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]

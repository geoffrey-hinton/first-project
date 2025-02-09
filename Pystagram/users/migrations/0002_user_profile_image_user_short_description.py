# Generated by Django 5.1.4 on 2025-01-24 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='users/profile', verbose_name='profile_image'),
        ),
        migrations.AddField(
            model_name='user',
            name='short_description',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
    ]

# Generated by Django 2.2.17 on 2024-03-11 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('typerush', '0008_auto_20240311_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='profile_images'),
        ),
    ]

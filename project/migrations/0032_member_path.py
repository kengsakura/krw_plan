# Generated by Django 3.2 on 2021-06-08 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0031_auto_20210607_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='path',
            field=models.ImageField(blank=True, default='profile/blank_profile.png', null=True, upload_to='profile/'),
        ),
    ]

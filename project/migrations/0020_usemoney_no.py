# Generated by Django 3.2 on 2021-05-24 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0019_usemoney'),
    ]

    operations = [
        migrations.AddField(
            model_name='usemoney',
            name='no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.2 on 2021-05-16 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0015_baseschooldata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='minoractivity',
            name='introduction',
        ),
        migrations.AddField(
            model_name='minoractivity',
            name='cutoff',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]

# Generated by Django 3.2 on 2021-05-16 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0017_auto_20210517_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minoractivity',
            name='cutoff',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
    ]

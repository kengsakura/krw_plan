# Generated by Django 3.2 on 2021-06-17 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_studentdata_th_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('classroom', models.IntegerField(blank=True, null=True)),
                ('room', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]

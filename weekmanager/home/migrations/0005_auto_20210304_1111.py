# Generated by Django 3.1.7 on 2021-03-04 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_day_pretty_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='date_end',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='date_start',
        ),
        migrations.AddField(
            model_name='activity',
            name='time_end',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='time_start',
            field=models.TimeField(null=True),
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-02 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_day_pretty_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day',
            name='pretty_date',
        ),
    ]

# Generated by Django 2.2.12 on 2020-05-23 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='startDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='startEnd',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

# Generated by Django 2.2.12 on 2020-05-24 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20200524_0811'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
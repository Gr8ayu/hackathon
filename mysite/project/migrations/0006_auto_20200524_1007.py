# Generated by Django 2.2.12 on 2020-05-24 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_task_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.ImageField(default='categories/default.jpeg', upload_to='categories/'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='icon',
            field=models.ImageField(default='tasks/default.jpeg', upload_to='tasks/'),
        ),
    ]
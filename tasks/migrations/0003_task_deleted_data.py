# Generated by Django 5.1.3 on 2024-11-14 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='deleted_data',
            field=models.BooleanField(default=False),
        ),
    ]
# Generated by Django 4.1.4 on 2023-03-06 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("scheduler", "0002_remove_code_project_remove_relation_project"),
    ]

    operations = [
        migrations.AddField(
            model_name="activity",
            name="progress",
            field=models.IntegerField(default=0),
        ),
    ]
# Generated by Django 4.1.4 on 2023-03-11 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("scheduler", "0007_alter_relation_predecessor"),
    ]

    operations = [
        migrations.AddField(
            model_name="activity",
            name="critical",
            field=models.BooleanField(default=False),
        ),
    ]

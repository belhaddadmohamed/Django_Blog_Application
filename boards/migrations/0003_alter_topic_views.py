# Generated by Django 4.1 on 2022-08-31 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("boards", "0002_topic_views"),
    ]

    operations = [
        migrations.AlterField(
            model_name="topic",
            name="views",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
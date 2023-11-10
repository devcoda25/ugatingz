# Generated by Django 4.2.7 on 2023-11-10 03:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("topics", "0005_alter_topic_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="topic",
            options={"verbose_name": "topic", "verbose_name_plural": "topics"},
        ),
        migrations.AlterField(
            model_name="topic",
            name="comments",
            field=models.ManyToManyField(related_name="topics", to="topics.comment"),
        ),
    ]

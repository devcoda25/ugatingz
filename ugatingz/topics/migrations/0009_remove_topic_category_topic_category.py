# Generated by Django 4.2.7 on 2023-11-10 05:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("topics", "0008_alter_section_content"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="topic",
            name="category",
        ),
        migrations.AddField(
            model_name="topic",
            name="category",
            field=models.ManyToManyField(related_name="topics", to="topics.category"),
        ),
    ]
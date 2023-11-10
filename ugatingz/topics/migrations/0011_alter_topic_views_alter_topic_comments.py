# Generated by Django 4.2.7 on 2023-11-10 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("topics", "0010_topic_content_alter_comment_text_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="topic",
            name="Views",
            field=models.ForeignKey(
                blank=True,
                default=0,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="topics.views",
            ),
        ),
        migrations.AlterField(
            model_name="topic",
            name="comments",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="topics", to="topics.comment"
            ),
        ),
    ]

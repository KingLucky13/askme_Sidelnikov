# Generated by Django 4.2.16 on 2024-11-13 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_question_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='likes',
        ),
    ]

# Generated by Django 4.2.16 on 2024-11-13 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_like_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='likes',
            field=models.ManyToManyField(to='app.like'),
        ),
        migrations.AddField(
            model_name='question',
            name='likes',
            field=models.ManyToManyField(to='app.like'),
        ),
        migrations.AlterUniqueTogether(
            name='answerlike',
            unique_together={('answer', 'like')},
        ),
        migrations.AlterUniqueTogether(
            name='questionlike',
            unique_together={('question', 'like')},
        ),
    ]
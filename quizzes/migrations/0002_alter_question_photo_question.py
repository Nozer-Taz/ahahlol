# Generated by Django 4.0.6 on 2022-08-03 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='photo_question',
            field=models.ImageField(blank=True, null=True, upload_to='question-images'),
        ),
    ]

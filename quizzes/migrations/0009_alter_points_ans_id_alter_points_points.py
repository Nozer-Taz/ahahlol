# Generated by Django 4.0.6 on 2022-08-09 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0008_points_ans_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='points',
            name='ans_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='points',
            name='points',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]

# Generated by Django 4.0.6 on 2022-08-09 11:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_group_alter_customuser_group'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quizzes', '0006_alter_answer_question_alter_question_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Points',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timer', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='answer',
            name='points',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='timer',
        ),
        migrations.AlterField(
            model_name='test',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.group'),
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.AddField(
            model_name='points',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.answer'),
        ),
        migrations.AddField(
            model_name='points',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.group'),
        ),
        migrations.AddField(
            model_name='points',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.question'),
        ),
        migrations.AddField(
            model_name='points',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.test'),
        ),
        migrations.AddField(
            model_name='points',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

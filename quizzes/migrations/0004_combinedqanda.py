# Generated by Django 4.0.6 on 2022-08-08 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0003_alter_answer_points_alter_answer_timer'),
    ]

    operations = [
        migrations.CreateModel(
            name='CombinedQandA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.question')),
            ],
        ),
    ]

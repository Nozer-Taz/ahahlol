from django.db import models

from accounts.models import CustomUser, Group


class Test(models.Model):
    test_name = models.CharField(max_length=200)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.test_name


class Question(models.Model):
    question = models.TextField()
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    photo_question = models.ImageField(upload_to='question-images', blank=True, null=True)
    activity = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.test} -> {self.question}'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer = models.TextField()
    is_correct = models.BooleanField(default=False)
    # timer = models.IntegerField(blank=True, null=True)
    # points = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.question} -> {self.answer}'


class Points(models.Model):
    timer = models.IntegerField(default=0)
    ans_id = models.IntegerField(blank=True, null=True)
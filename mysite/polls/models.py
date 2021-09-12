import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


# Create your models here.

class Question(models.Model):
    question_text = models.CharField('问题正文', max_length=200)
    pub_date = models.DateTimeField('发布时间')

    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='最近发表的吗？',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


# def vote_count(id):
#     """Return total votes for a given poll. id is poll id"""
#     if id <= Question.objects.count():
#         question = Question.objects.get(id=id)
#         count = 0
#         choiceSet = question.choice_set

#         for i in range(choiceSet.count()):
#             count += choiceSet.all()[i].votes
        
#         return count 
#     else: 
#         raise ValueError


# def find_polls_for_text(text):
#     """Return list of Question objects for all polls containing some text"""       
#     q_list = Question.objects.filter(question_text__icontains = text)
#     return q_list


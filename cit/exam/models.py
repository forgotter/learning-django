from django.db import models

class Question(models.Model):
    question_text = models.TextField(max_length=200)
    optionA = models.CharField(max_length=100, default='None of given')
    optionB = models.CharField(max_length=100, default='None of given')
    optionC = models.CharField(max_length=100, default='None of given')
    optionD = models.CharField(max_length=100, default='None of given')
    answer_text = models.CharField(max_length=100, default='No answer selected')
    chapter = models.IntegerField(default = 1)
    def __str__(self):
        return str(self.question_text)

class Test(models.Model):
    id = models.IntegerField(default = 0, primary_key=True)
    name = models.CharField(default = 'No Name', max_length=100)
    score = models.IntegerField(default = 0)
    question = models.CharField(max_length=400, blank=True, null=True)
    answer = models.CharField(max_length=10000,  blank=True, null=True)
    def __str__(self):
        return str(self.name)+"\troll:"+str(self.roll)+"\tscore:"+str(self.score)

class FeedbackForm(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    f1 = models.TextField()
    f2 = models.TextField()
    f3 = models.TextField()
    f4 = models.TextField()
    f5 = models.TextField()

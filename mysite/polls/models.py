from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200) #질문
    pub_date = models.DateTimeField('date published') #날짜
    def __str__(self):
        return self.question_text
        
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #Question에 키를 넣지 않고 클래스 자체를 넣는다. # Django의 특징
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return str(self.question)+self.choice_text + str(self.votes)
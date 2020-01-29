from django.db import models

# Create your models here.
class Curriculum(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self): #객체를 출력했을 때 찍어져 나오는 모습을 담당
        return str(self.id)+'번/' + self.name


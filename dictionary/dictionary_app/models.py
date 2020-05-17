from django.db import models

# Create your models here.

class DictionaryDB(models.Model):
    letter = models.CharField(max_length = 1)
    word = models.CharField(max_length = 30)
    defination = models.CharField(max_length = 60)
    example = models.CharField(max_length = 90)

    def ___str__(self):
        return"%s %s"%(self.letter, self.word)


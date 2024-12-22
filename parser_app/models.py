from django.db import models

class KnigoGid(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    grade = models.FloatField(blank=True)
    
    def __str__(self):
        return self.title
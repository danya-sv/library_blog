from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.name
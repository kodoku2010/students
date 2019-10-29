from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    group = models.CharField(max_length=8)
    mark = models.IntegerField()
    city = models.CharField(max_length=100)
    year = models.IntegerField()
    gender = models.BooleanField()

    def __str__(self):
        return self.name + self.last_name
    
    class Meta:
        ordering = ["-mark"]


from django.db import models

# Create your models here.
class Classes(models.Model):
    title = models.CharField(max_length=32)
    teachers = models.ManyToManyField('Teachers')
    def __str__(self):
        return self.title

class Teachers(models.Model):
    name = models.CharField(max_length=32)

class Students(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.BooleanField()
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

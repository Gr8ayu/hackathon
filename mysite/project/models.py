from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='categories/', blank='categories/default.jpeg')
    color = models.CharField(max_length=200, default="#000000")

    def __str__(self):
        return self.name

class Task(models.Model):
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.ImageField(upload_to='tasks/',  blank='tasks/default.jpeg')
    startDate = models.DateTimeField(blank=True,null=True)
    startEnd = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.name

class Agenda(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    def __str__(self):
        return self.task.name
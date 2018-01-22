from django.db import models

# Create your models here.


class Todo(models.Model):
    """这是一个todo类"""
    task = models.CharField(max_length=1000)

    def __str__(self):
        return self.task

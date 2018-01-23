from django.db import models

# Create your models here.

# 添加一个todo管理类
# 这是继承models.Manager类
class TodoManager(models.Manager):
    def get_queryset(self):
        return super(TodoManager, self).get_queryset().filter(is_delete=False)

    def new(self, task):
        m = Todo()
        m.task = task
        m.is_delete = False
        m.save()
        return m



class Todo(models.Model):
    """这是一个todo类"""
    task = models.CharField(max_length=1000)
    is_delete = models.BooleanField(default=False)

    # 添加一个属性来调用TodoManage()
    todo = TodoManager()

    def __str__(self):
        return self.task

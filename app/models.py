from django.db import models
import time

# Create your models here.


def format_time():
    # time.time()返回的是 unix time
    # 如何把 unix time 转化为普通人可以看的格式
    formatx = "%Y/%m/%d %H:%M:%S"
    value = time.localtime(int(time.time()))
    ct = time.strftime(formatx, value)
    return ct

# 添加一个todo管理类
# 这是继承models.Manager类
class TodoManager(models.Manager):
    def get_queryset(self):
        return super(TodoManager, self).get_queryset().filter(is_delete=False)

    def new(self, task):
        m = Todo()
        m.task = task
        m.is_delete = False
        m.ct = format_time()
        m.save()
        return m



class Todo(models.Model):
    """这是一个todo类"""
    task = models.CharField(max_length=1000)
    is_delete = models.BooleanField(default=False)
    ct = models.CharField(max_length=50)

    # 添加一个属性来调用TodoManage()
    todo = TodoManager()

    def __str__(self):
        return self.task

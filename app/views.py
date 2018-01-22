from django.shortcuts import render
# from django.http import *
# from django.template import RequestContext, loader
from .models import Todo


# Create your views here.

# 测试
# def index(request):
#     return HttpResponse("hello world")

# def index(request):
#     返回模板对象
#     temp = loader.get_template("todo/index.html")
#     return HttpResponse(temp.render())

def index(request):
    todo_list = Todo.objects.all()

    print("todo_list", todo_list)
    # context 是一个字典
    context = dict(
        todo_list=todo_list,
    )
    # 和jinja2渲染方式类似
    return render(request, "todo/index.html", context)





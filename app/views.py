from django.shortcuts import render
# from django.http import *
# from django.template import RequestContext, loader
from .models import Todo
# from django.template.context_processors import csrf

# Create your views here.

# 测试
# def index(request):
#     return HttpResponse("hello world")

# def index(request):
#     返回模板对象
#     temp = loader.get_template("todo/index.html")
#     return HttpResponse(temp.render())

# def index(request):
#     todo_list = Todo.objects.all()
#     # context 是一个字典
#     context = dict(
#         todo_list=todo_list,
#     )
#     # 和jinja2渲染方式类似
#     return render(request, "todo/index.html", context)

def index(request):
    # 获取task
    if request.method == "POST":
        print("post", request.POST)
        task = request.POST["task"]
        # 保存task
        print("task", task)
        m = Todo.todo.new(task)
        print("m", m)
    # 重写了管理类就没有objects属性
    # todo_list = Todo.objects.all()
    todo_list = Todo.todo.filter(is_delete=False)

    # context 是一个字典
    context = dict(
        todo_list=todo_list,
    )
    # context.update(csrf(request))
    # 和jinja2渲染方式类似
    return render(request, "todo/index.html", context)








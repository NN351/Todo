from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo


def homepage(request):
    todo_list = ToDo.objects.all()
    return render(request, "index.html", {"todo_list": todo_list})


def test(request):
    return render(request, "test.html")

def check(request):
    return HttpResponse("текшируу")


def add_todo(request):
    f = request.POST
    text = f["todo_text"]
    todo = ToDo(
        text=text
    )
    todo.save()
    return redirect(homepage)


def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(homepage)


def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = not todo.is_favorite
    todo.save()
    return redirect(homepage)

def close_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(homepage)
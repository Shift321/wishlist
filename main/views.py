from typing import Text

from django.http import request
from main.models import ToDoList,Item
from django.shortcuts import render,redirect
from .forms import CreateNewList


def index(response,id):
    ls = ToDoList.objects.get(id=id)
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c"+str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")
            if len(txt)> 2:
                ls.item_set.create(text=txt,complete=False)
            else:
                print("invalid")
    return render(response,"main/list.html",{"ls":ls})


def home(response):
    return render(response,"main/home.html",{})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            data = form.cleaned_data["name"]
            t = ToDoList(name=data)
            t.save()
            response.user.todolist.add(t)
        
        return redirect("/%i" %t.id)
    else:
        form = CreateNewList()
    return render(response,"main/create.html",{"form":form})

def show_all(response):
    all = ToDoList.objects.all()
    return render(response,"main/views.html",{"all":all})


def deleteitem(response,id):
    tds = Item.objects.get(id=id)
    tds_id = tds.todolist.id
    tds.delete()
    return redirect(f"/{tds_id}")


def deleteobject(response,id):
    wish_list = ToDoList.objects.get(id=id)
    wish_list.delete()
    return redirect("/view")

def my_wish_list(response):
    all = ToDoList.objects.all()
    return render(response,"main/mywishlists.html",{"all":all})
from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.



@login_required
def dashboard(request):
    user = User.objects.get(pk=1)
    agenda = Agenda.objects.filter(user = user)

    print(agenda)
    return render(request,'project/dashboard.html',{'tasks':agenda})

def listCategories(request):
    cat = Category.objects.all()
    print(cat)
    return render(request,'project/category.html',{'cat':cat})

def task(request,category):
    tasks = Task.objects.filter(category_id=category)
    # print(cat[0].icon.__dict__)
    return render(request,'project/task.html',{'tasks':tasks})

def addAgenda(request,id, **kwargs):
    # cat = Task.objects.filter(category_id=category)
    # print(cat[0].icon.__dict__)

    try:
        agenda = Agenda.objects.get(task_id = id)
        # print("FOUND", agenda)
        agenda.delete()
    except ObjectDoesNotExist as e:
        print(e)
        NewAgenda = Agenda()
        NewAgenda.user = User.objects.get(id=1)
        NewAgenda.task = Task.objects.get(id=id)
        NewAgenda.save()
    # return render(request,'project/task.html',{'cat':cat})
    return redirect("/dashboard")

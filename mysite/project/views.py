from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.


def listCategories(request):
    cat = Category.objects.all()
    print(cat)
    return render(request,'project/category.html',{'cat':cat})

def category(request,category):
    cat = Task.objects.filter(category_id=category)
    # print(cat[0].icon.__dict__)
    return render(request,'project/category.html',{'cat':cat})

@login_required
def dashboard(request):
    user = User.objects.get(pk=1)
    agenda = Agenda.objects.filter(user = user)
    #print(agenda)
    return render(request,'logged_out.html')
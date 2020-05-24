from django.urls import include
from django.contrib import admin
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from .views import *

def function():
    pass


urlpatterns = [
    # path('',dashboard, name="dashboard"),
    path('',dashboard, name="dashboard"),
    path('add/<int:id>/',addAgenda, name="dashboard"),
    path('category/',listCategories, name="categories"),
    path('category/<int:category>/',task, name="tasks"),
    path('category/<int:category>/add/<int:id>/',addAgenda, name="tasks"),
    
]

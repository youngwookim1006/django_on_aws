from django.urls import path

from .views import select_todolist, update_todo, delete_todo

# http://localhost:8000/*
urlpatterns = [
    # http://localhost:8000/
    path("",select_todolist, name="todolist"),
    # http://localhost:8000/update/id
    path("update/<int:id>", update_todo, name="update-task"),
    # http://localhost:8000/update/id
    path("delete/<int:id>", delete_todo, name="delete-task"),
]
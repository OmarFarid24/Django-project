from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import ToDoList, Tag, Task

admin.site.register(ToDoList)
admin.site.register(Tag)
admin.site.register(Task)
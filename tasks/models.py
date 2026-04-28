from django.db import models

# Create your models here.

from django.conf import settings
from django.db import models


class ToDoList(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='todo_lists'
    )

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)
    priority = models.IntegerField()
    todo_list = models.ForeignKey(
        ToDoList,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='tasks'
    )

    def __str__(self):
        return self.title
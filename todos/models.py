from django.db import models
from django.contrib.auth.models import User
from .abstracts import AbstractDatesModel


class TodoModel(AbstractDatesModel):
    title = models.CharField(max_length=200)
    actor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_todos')
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_todos')
    completed = models.BooleanField(default=False)

    class Meta:
        db_table = 'todos'
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


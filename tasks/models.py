from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ListTask(models.Model):
    # user = models.ForeignKey(User , on_delete=models.CASCADE, related_name='list_tasks')
    name = models.CharField(max_length=150)
    pub_date = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Task(models.Model):
    list_tasks = models.ForeignKey(ListTask, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    pub_date = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
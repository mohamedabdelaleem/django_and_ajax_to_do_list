from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey( User , on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=150)
    pub_date = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
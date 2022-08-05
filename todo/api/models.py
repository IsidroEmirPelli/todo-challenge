from django.db import models

# Create your models here.


class Task(models.Model):
    fecha = models.DateTimeField(auto_now_add=True,  blank=True)
    content = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

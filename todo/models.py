from django.db import models


class Task(models.Model):
    task_text = models.CharField(max_length=160)
    deadline = models.DateField('deadline')
    progress = models.FloatField('progress')
    pub_date = models.DateTimeField('date published')

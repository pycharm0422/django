from django.db import models

class ToDoList(models.Model):
    full_note = models.CharField(max_length=200, null=True)
    date_time = models.DateTimeField(auto_now_add=True)
    important = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.full_note

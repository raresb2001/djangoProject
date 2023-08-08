from django.contrib.auth.models import User
from django.db import models

from student.models import Student


class History(models.Model):
    message = models.TextField(max_length=400)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.message


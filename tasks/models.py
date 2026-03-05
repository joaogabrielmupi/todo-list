from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    #Ordenacao
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
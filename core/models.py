from django.db import models


# Create your models here.
class Message(models.Model):
    message = models.CharField(max_length=1000)
    device = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.message} - {self.device}"

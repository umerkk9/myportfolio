from django.db import models
from django.db import models

class ContactMessage(models.Model):
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.email}"

# Create your models here.

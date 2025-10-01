from django.db import models

class Conversation(models.Model):
    prompt = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    response = models.TextField(null=True, blank=True)
    metadata = models.JSONField(null=True, blank=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.timestamp}: {self.prompt[:50]}..."
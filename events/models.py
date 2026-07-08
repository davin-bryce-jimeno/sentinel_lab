from django.db import models

# Create your models here.
class LoginEvent(models.Model):
    class Status(models.TextChoices):
        SUCCESS = "SUCCESS", "Success"
        FAILED = "FAILED", "Failed"

    ip_address = models.GenericIPAddressField()
    username = models.CharField()
    status = models.CharField(max_length=10, choices=Status.choices)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return f"{self.status} {self.username}@{self.ip_address}"



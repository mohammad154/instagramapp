from django.db import models

from user.models import Person


class Notification(models.Model):
    sender = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="receiver")
    read = models.BooleanField(default=False)
    message = models.CharField(max_length=100)
    time = models.DateTimeField()

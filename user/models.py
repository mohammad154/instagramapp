from django.contrib.auth.models import User
from django.db import models


class Person(User):
    dob = models.DateField(null=True)
    accept = models.BooleanField(null=False, default=False)
    pic = models.ImageField(upload_to="profilepic/%y", null=True)
    bio = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=70, null=True)
    country = models.CharField(max_length=70, null=True)
    profession = models.CharField(max_length=80, null=True)
    bgpic = models.ImageField(upload_to="bg_pic/%y", null=True)
    followers = models.IntegerField(default=0)


class Following(models.Model):
    follower = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="follower")
    following = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="following")

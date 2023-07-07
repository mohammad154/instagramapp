from django.db import models

from user.models import Person


class Post(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    time = models.DateTimeField()
    type = models.CharField(max_length=20)
    desc = models.CharField(max_length=150, null=True)
    video = models.FileField(upload_to='videos/%y', null=True)
    image = models.ImageField(upload_to='images/%y', null=True)
    text = models.TextField(max_length=1500, null=True)
    likes = models.IntegerField(default=0)


class Liked(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    liked = models.IntegerField()
    comment = models.CharField(max_length=500, null=True)


class Comment(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=250)
    time = models.DateTimeField()

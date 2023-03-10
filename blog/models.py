from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog/')
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    def user_fullname(self):
        return self.user.get_full_name()

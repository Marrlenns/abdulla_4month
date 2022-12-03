from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(null=True)

    def __str__(self):
        return self.title


class Hashtag(models.Model):
    title = models.CharField(max_length=255)
    post = models.ManyToManyField(Post, blank=True, null=True)

    def __str__(self):
        return self.title
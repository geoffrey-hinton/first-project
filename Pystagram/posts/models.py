from django.db import models
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe


# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(
        "users.User",
        verbose_name = "Author",
        on_delete = models.CASCADE,
    )
    content = models.TextField("content")
    created = models.DateField("Created on", auto_now_add = True)

    tags = models.ManyToManyField("posts.HashTag", verbose_name = "list of HashTag", blank = True)

    def __str__(self):
        return f"{self.user.username}'s Post(id: {self.id})"

class PostImage(models.Model):
    post = models.ForeignKey(
        Post,
        verbose_name = "post",
        on_delete = models.CASCADE,
    )
    photo = models.ImageField(
        "Photo", upload_to = "post"
    )

class Comment(models.Model):
    user = models.ForeignKey(
        "users.User",
        verbose_name = "Author",
        on_delete = models.CASCADE,
    )
    post = models.ForeignKey(
        Post,
        verbose_name = "post",
        on_delete = models.CASCADE,
    )
    content = models.TextField("content")
    created = models.DateField("Created on", auto_now_add = True)

class HashTag(models.Model):
    name = models.CharField("Tag_name", max_length = 50)

    def __str__(self):
        return self.name


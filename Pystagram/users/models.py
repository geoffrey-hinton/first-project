from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    profile_image = models.ImageField(
        "profile_image", upload_to = "users/profile", blank = True
    )
    short_description = models.TextField("description", blank = True)

    like_posts = models.ManyToManyField(
        "posts.Post",
        verbose_name = "Liked Posts",
        related_name = "like_users",
        blank = True,
    )
    following = models.ManyToManyField(
        "self",
        verbose_name = "People i follow",
        related_name = "followers",
        symmetrical = False,
        through = "users.Relationship",
    )

    def __str__(self):
        return self.username

class Relationship(models.Model):
    from_user = models.ForeignKey(
        "users.User",
        verbose_name = "User who sent a follow request",
        related_name = "following_relationships",
        on_delete = models.CASCADE,
    )

    to_user = models.ForeignKey(
        "users.User",
        verbose_name = "User who requested to follow",
        related_name = "follower_relationships",
        on_delete = models.CASCADE,
    )

    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"relationship ({self.from_user}) -> ({self.to_user})"
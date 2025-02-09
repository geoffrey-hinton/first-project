from django.contrib import admin
from posts.models import Post, PostImage, Comment, HashTag
from django.contrib.admin.widgets import AdminFileWidget
from django.db import models
from django.utils.safestring import mark_safe
from django.db.models import ManyToManyField
from django.forms import CheckboxSelectMultiple
import admin_thumbnails


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1

class LikeUserInline(admin.TabularInline):
    model = Post.like_users.through
    verbose_name = "Liked User"
    verbose_name_plural = f"{verbose_name} list"
    extra = 1

    def has_change_permission(self, request, obj = None):
        return False

@admin_thumbnails.thumbnail("photo")
class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "content",
    ]
    inlines = [
        CommentInline,
        PostImageInline,
        LikeUserInline,
    ]
    formfield_overrides = {
        ManyToManyField: {"widget": CheckboxSelectMultiple},
    }

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "post",
        "photo",
    ]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "post",
        "content",
    ]

@admin.register(HashTag)
class HashTagAdmin(admin.ModelAdmin):
    pass
    # Post 변경 화면에서 ManyToMany를 Checkbox로 출력
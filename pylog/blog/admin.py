from django.contrib import admin
from blog.models import Post
from blog.models import Comment

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "thumbnail"]
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


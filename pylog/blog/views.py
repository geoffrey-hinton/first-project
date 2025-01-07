from django.shortcuts import render
from blog.models import Post
from blog.models import Comment

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    print(posts)
    context = {
        "posts" : posts,
    }

    return render(request, "post_list.html", context)

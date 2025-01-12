from django.shortcuts import render
from django.shortcuts import redirect
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

def post_detail(request, post_id):
    post = Post.objects.get(id = post_id)

    # print(post.content)
    context = {
        "post" : post
    }

    if request.method == "POST":
        Comment.objects.create(
            post = post,
            content = request.POST.get("comment"),
        )

    return render(request, "post_detail.html", context)

def post_add(request):
    if request.method == "POST":
        print("method POST")
        thumbnail = request.FILES.get('thumbnail')
        title = request.POST.get("title")
        content = request.POST["content"]
        post = Post.objects.create(
            title = title,
            content = content,
            thumbnail = thumbnail,
        )
        return redirect(f"/posts/{post.id}/")


    else:
        print("method GET")

    return render(request, "post_add.html")

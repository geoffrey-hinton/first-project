from django.shortcuts import render, redirect
from posts.models import Post, Comment, PostImage, HashTag
from posts.forms import CommentForm, PostForm
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse

# Create your views here.

def feeds(request):

    posts = Post.objects.all()
    comment_form = CommentForm()
    context = {
        "posts" : posts,
        "comment_form" : comment_form,
    }
    return render(request, "posts/feeds.html", context)

@require_POST

def comment_add(request):
    print(require_POST)

    form = CommentForm(data = request.POST)
    print(request.user)
    print(form.is_valid())

    if form.is_valid():
        # commit = False option을 이용해서 메모리상에 Commit 객체 생성
        comment = form.save(commit = False)

        comment.user = request.user

        comment.save()

        print(comment.id)
        print(comment.content)
        print(comment.user)
        if request.GET.get("next"):
            url_next = request.GET.get('next')
        else:
            url_next = reverse("posts:feeds") + f"#post-{comment.post.id}"

        return HttpResponseRedirect(url_next)

@require_POST
def comment_delete(request, comment_id):
    if request.method == "POST":
        comment = Comment.objects.get(id=comment_id)
        if comment.user == request.user:
            comment.delete()
            url = reverse("posts:feeds") + f"#post-{comment.post.id}"
            return HttpResponseRedirect(url)
        else:
            return HttpResponseForbidden("you don't have permission to delete tins comment")

def post_add(request):
    if request.method == "POST":
        # request.POST로 온 데이터 ("content"는 PostForm으로 처리
        form = PostForm(data = request.POST)

        if form.is_valid():
            # Post의 "user" 값은 request에거 가져와 자동 할당한다.
            post = form.save(commit = False)
            post.user = request.user
            post.save()

            for image_file in request.FILES.getlist("images"):
                # request.FILES 또는 request.FILES.getlist()로 가져온 파일들은
                # Model의 ImageField 부분에 곧바로 할당된다.
                PostImage.objects.create(
                    post = post,
                    photo = image_file,
                )
            # Post의 생성이 완료되면, 생성된 Post의 위치로 이동하도록 한다.
            tag_string = request.POST.get("tags")
            tag_list = [i.strip() for i in tag_string.split(",")]
            print(tag_list)
            for tag_name in tag_list:
                tag, _= HashTag.objects.get_or_create(name = tag_name)
                print(tag)
                post.tags.add(tag)
            url = reverse("posts:feeds") + f"#post-{post.id}"
            return HttpResponseRedirect(url)
    else:
        form = PostForm()

        context = {
            "form" : form
        }

        return render(request, "posts/post_add.html", context)

def tags(request, tag_name):
    try:
        tag = HashTag.objects.get(name = tag_name)
    except HashTag.DoesNotExist:
        #tag_name에 해당하는 HashTag를 찾지 못한 경우, 빈 Query를 돌려준다.
        posts = Post.objects.none()
    else:
        posts = Post.objects.filter(tags = tag)

    context = {
        "tag_name" : tag_name,
        "posts" : posts,
    }
    return render(request, "posts/tags.html", context)

def post_detail(request, post_id):
    post = Post.objects.get(id = post_id)
    comment_form = CommentForm()
    context = {
        "post" : post,
        "comment_form" : comment_form,
    }

    return render(request, "posts/post_detail.html", context)

def post_like(request, post_id):
    post = Post.objects.get(id = post_id)
    user = request.user

    if user.like_posts.filter(id = post.id).exists():
        user.like_posts.remove(post)
    else:
        user.like_posts.add(post)

    url_next = request.GET.get("next") or reverse("posts:feeds") + f"#post-{post.id}"

    return HttpResponseRedirect(url_next)



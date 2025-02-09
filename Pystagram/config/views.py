from django.shortcuts import render, redirect

def index(request):
    if not request.user.is_authenticated:
        return redirect("users:login")
    else:
        return redirect("posts:feeds")

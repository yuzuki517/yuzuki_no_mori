import markdown
from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.order_by("-created_at")
    return render(request, "blog/index.html", {"posts": posts})

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.body_html = markdown.markdown(
        post.body,
        extensions=["fenced_code", "codehilite"]
    )
    return render(request, "blog/detail.html", {"post": post})

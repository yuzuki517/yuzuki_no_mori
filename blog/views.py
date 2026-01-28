import markdown
from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.order_by("-created_at")
    return render(
        request,
        "blog/list.html",
        {"posts": posts},
    )

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(
        request,
        "blog/detail.html",
        {"post": post},
    )

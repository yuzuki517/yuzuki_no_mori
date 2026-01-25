from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.order_by("-created_at")
    return render(request, "blog/index.html", {"posts": posts})

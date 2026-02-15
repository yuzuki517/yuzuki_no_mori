import markdown
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Post, Category
from taggit.models import Tag

# Create your views here.
def post_list(request):
    posts = Post.objects.order_by("-created_at")
    return render(request, "blog/post_list.html", {"posts": posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/detail.html", {"post": post})

class PostListView(ListView):
    model = Post
    paginate_by = 10
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    queryset = Post.objects.order_by("-created_at")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ["list_title"] = "最新記事"
        return context

class CategoryListView(PostListView):
    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs["slug"])
        return super().get_queryset().filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list_title"] = f"カテゴリ：{self.category.name}"
        return context

class TagListView(PostListView):
    def get_queryset(self):
        self.tag = get_object_or_404(Tag, slug=self.kwargs["slug"])
        return super().get_queryset().filter(tags__slug=self.tag.slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list_title"] = f"タグ：{self.tag.name}"
        return context

class ArchiveListView(PostListView):
    def get_queryset(self):
        year = self.kwargs["year"]
        month = self.kwargs["month"]
        return super().get_queryset().filter(
            created_at__year=year,
            created_at__month=month
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list_title"] = f"{self.year}年{self.month}月の記事"
        return context

class PostSearchView(PostListView):
    def get_queryset(self):
        q = self.request.GET.get("q", "").strip()
        if not q:
            return Post.objects.none()
        qs = super().get_queryset()
        return qs.filter(Q(title__icontains=q) | Q(body__icontains=q)).order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list_title"] = f"「{self.query}」の検索結果"
        return context

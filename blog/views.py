import markdown
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Post, Category
from taggit.models import Tag

# Create your views here.
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

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/detail.html"
    context_object_name = "post"
    slug_field = "slug"
    slug_url_kwarg = "slug"

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
        self.year = self.kwargs["year"]
        self.month = self.kwargs["month"]
        return super().get_queryset().filter(
            created_at__year=self.year,
            created_at__month=self.month
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list_title"] = f"{self.year}年{self.month}月の記事"
        return context

class PostSearchView(PostListView):
    def get_queryset(self):
        self.query = self.request.GET.get("q", "").strip()
        if not self.query:
            return Post.objects.none()
        return super().get_queryset().filter(
            Q(title__icontains=self.query) | Q(body__icontains=self.query)).order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list_title"] = f"「{self.query}」の検索結果"
        return context

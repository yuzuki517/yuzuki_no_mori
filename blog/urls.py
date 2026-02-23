from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    CategoryListView, 
    TagListView, 
    ArchiveListView, 
    PostSearchView,
)

app_name = "blog"

urlpatterns = [
    # 検索
    path('search/', PostSearchView.as_view(), name='post_search'),
    path('search/page/<int:page>/', PostSearchView.as_view(), name='post_search_paginated'),
    # 詳細
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    # カテゴリ
    path('category/<slug:slug>/page/<int:page>/', CategoryListView.as_view(), name='category_posts_paginated'), 
    path('category/<slug:slug>/', CategoryListView.as_view(), name='category_posts'), 
    # タグ
    path('tag/<slug:slug>/page/<int:page>/', TagListView.as_view(), name='tag_posts_paginated'), 
    path('tag/<slug:slug>/', TagListView.as_view(), name='tag_posts'), 
    # アーカイブ
    path('archive/<int:year>/<int:month>/page/<int:page>/', ArchiveListView.as_view(), name='archive_posts_paginated'), 
    path('archive/<int:year>/<int:month>/', ArchiveListView.as_view(), name='archive_posts'), 
    # 一覧ページネーション
    path("page/<int:page>/", PostListView.as_view(), name="post_list_paginated"),
    # トップページ
    path('', PostListView.as_view(), name='post_list'), 
]

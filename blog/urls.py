from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('category/<slug:slug>/', views.CategoryListView.as_view(), name='category_posts'), 
    path('category/<slug:slug>/page/<int:page>/', views.CategoryListView.as_view(), name='category_posts_paginated'), 
    path('tag/<slug:slug>/', views.TagListView.as_view(), name='tag_posts'), 
    path('tag/<slug:slug>/page/<int:page>/', views.TagListView.as_view(), name='tag_posts_paginated'), 
    path('archive/<int:year>/<int:month>/', views.ArchiveListView.as_view(), name='archive_posts'), 
    path('archive/<int:year>/<int:month>/page/<int:page>/', views.ArchiveListView.as_view(), name='archive_posts_paginated'), 
    path("page/<int:page>/", views.PostListView.as_view(), name="post_list_paginated"),
    path('search/', views.PostSearchView.as_view(), name='post_search'),
    path('search/page/<int:page>/', views.PostSearchView.as_view(), name='post_search_paginated'),
    path('', views.PostListView.as_view(), name='post_list'), 
]

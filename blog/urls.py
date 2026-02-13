from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'), 
    path('category/<slug:slug>/', views.CategoryListView.as_view(), name='category_posts'), 
    path('tag/<slug:slug>/', views.TagListView.as_view(), name='tag_posts'), 
    path('archive/<int:year>/<int:month>/', views.ArchiveListView.as_view(), name='archive_posts'), 
    path('search/', views.PostSearchView.as_view(), name='post_search'),
]

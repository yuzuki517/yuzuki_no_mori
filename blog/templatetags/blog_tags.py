from django import template
from django.db.models import Count
from ..models import Post, Category
from taggit.models import Tag

register = template.Library()

@register.inclusion_tag('blog/tags/category_list.html', takes_context=True)
def category_list(context):
    categories = Category.objects.annotate(count=Count('posts')).order_by('-count')
    return {'categories': categories, 'request': context.get('request')}

@register.inclusion_tag('blog/tags/tag_list.html', takes_context=True)
def tag_list(context):
    tags = Tag.objects.annotate(num_posts=Count('taggit_taggeditem_items')).filter(num_posts__gt=0).order_by('-num_posts', 'name')[:50]
    return {'tags': tags, 'request': context.get('request')}

@register.inclusion_tag('blog/tags/archives.html', takes_context=True)
def archives(context):
    dates = Post.objects.dates('created_at', 'month', order='DESC')
    return {'dates': dates, 'request': context.get('request')}

@register.inclusion_tag('blog/tags/recent_posts.html', takes_context=True)
def recent_posts(context, num=3):
    posts = Post.objects.order_by('-created_at')[:num]
    return {'recent_posts': posts, 'request': context.get('request')}

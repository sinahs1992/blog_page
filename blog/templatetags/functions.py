from django import template
from blog.models import Post, Category
from django.db.models import Count
from django.utils import timezone
from blog.models import Post
register = template.Library()


# @register.simple_tag(name="view_increase")
# def function(post):
#     post.view_count += 1
#     post.save()

@register.simple_tag(name='posts')
def function():
    posts = Post.objects.all()
    return posts

@register.filter
def snippet(text, number):
    return text[:number] + '...'

@register.inclusion_tag('blog/pop_category.html')
def popular_categories(arg=7):
    categories = Category.objects.annotate(category_count=Count('post')).order_by('-category_count')[:arg]
    return { "categories": categories }

@register.inclusion_tag('blog/recent_posts.html')
def recent_posts(arg=3):
    now = timezone.now()
    recent_posts = Post.objects.filter(status=True, published_date__lte=now).order_by('-published_date')[:arg]
    return { 'recent_posts': recent_posts }


@register.inclusion_tag('blog/pop_posts.html')
def popular_posts(args=3):
    now = timezone.now()
    popular_posts = Post.objects.filter(status=True, published_date__lte=now).order_by('-view_count')[:args]
    return {'popular_posts': popular_posts}
from django import template
from blog.models import Post, Category
from django.db.models import Count
from django.utils import timezone

register = template.Library()


@register.simple_tag(name="view_increase")
def function(post):
    post.view_count += 1
    post.save()



@register.inclusion_tag('blog/pop_category.html')
def popular_categories():
    categories = Category.objects.annotate(category_count=Count('post')).order_by('-category_count')[:7]
    return { "categories": categories }

@register.inclusion_tag('blog/recent_posts.html')
def recent_posts():
    now = timezone.now()
    recent_posts = Post.objects.filter(status=True, published_date__lte=now).order_by('-published_date')[:3]
    return { 'recent_posts': recent_posts }
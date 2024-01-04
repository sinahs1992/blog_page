from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone

def home_blog(request):
    current_time =timezone.now()
    posts = Post.objects.filter(published_date__lte=current_time, status=True)
    return render(request, 'blog/blog-home.html', {'posts': posts})     

def single_blog(request, slug):

    current_time =timezone.now()
    published_posts = Post.objects.filter(published_date__lte=current_time, status=True)
    post = get_object_or_404(published_posts, slug=slug)
    next_post = published_posts.filter(published_date__gt=post.published_date).order_by('published_date').first()
    previous_object = published_posts.filter(published_date__lt=post.published_date).order_by('-published_date').first()
    context = {'post': post, 'next_post':next_post, 'previous_object':previous_object}
    return render(request, 'blog/blog-single.html', context)

def test(request):
    current_time =timezone.now()
    posts = Post.objects.filter(status=True, published_date__lte=current_time)
    current = None
    archive = {}
    for post in posts:
        year = post.published_date.year
        if current != year:
            current = year
            archive[year] = [post]
        else:
            archive[year].append(post)
    context = {'archive':archive}
    return render(request, 'test.html', context)

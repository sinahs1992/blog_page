from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home_blog(request, **kwargs):
    current_time =timezone.now()
    posts = Post.objects.filter(published_date__lte=current_time, status=True)
    if kwargs.get('category_name'):
        posts = posts.filter(category__name=kwargs['category_name'])
    elif kwargs.get('tag_name'):
        posts = posts.filter(tag__name=kwargs['tag_name'])
    elif kwargs.get('author_username'):
        posts = posts.filter(author__username=kwargs['author_username'])

    posts = Paginator(posts, 4)
    try :
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
        page_range = posts.paginator.page_range
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(posts.num_pages)
    context = {'posts': posts, 'page_range': page_range}
    return render(request, 'blog/blog-home.html', context)     

def single_blog(request, slug):

    current_time =timezone.now()
    published_posts = Post.objects.filter(published_date__lte=current_time, status=True)
    post = get_object_or_404(published_posts, slug=slug)
    next_post = published_posts.filter(published_date__gt=post.published_date).order_by('published_date').first()
    previous_object = published_posts.filter(published_date__lt=post.published_date).order_by('-published_date').first()

    # increase view_count
    post.view_count += 1
    post.save()

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


def tag_test(request):
    return render(request, 'tag_test.html', {'example' : [2, 4, 6]})


def blog_search(request):
    current_time =timezone.now()
    posts = Post.objects.filter(published_date__lte=current_time, status=True)
    if request.method == "GET":
        if result := request.GET.get('s'):
            posts = posts.filter(Q(title__icontains=result) | Q(content__icontains=result))
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)
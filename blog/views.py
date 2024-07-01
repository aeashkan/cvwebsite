from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Post
from datetime import datetime
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def blog_view(request, cat_name=None, author_username=None, tag_name=None):
    posts = Post.objects.filter(status=1, published_date__lte=datetime.now()).order_by('-published_date')
    if cat_name:
        posts = posts.filter(category__name=cat_name)

    if author_username:
        posts = posts.filter(author__username=author_username)

    if tag_name:
        posts = posts.filter(tags__name__in=[tag_name])

    posts = Paginator(posts, 2)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)


    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)


def single_view(request, pid):
    post = get_object_or_404(Post, pk=pid, status=True, published_date__lte=datetime.now())
    previous_post = Post.objects.filter(published_date__lt=post.published_date).order_by('-published_date').first()
    next_post = Post.objects.filter(published_date__gt=post.published_date).order_by('published_date').first()
    post.counted_view += 1
    post.save()
    context = {'post': post,
               'previous_post': previous_post,
               'next_post': next_post,
               }
    return render(request, 'blog/single.html', context)

def blog_search(request):
    posts = Post.objects.filter(status=True, published_date__lte=datetime.now()).order_by('-published_date')
    if request.method == 'GET':
        posts = posts.filter(content__contains=request.GET.get('s'))
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)

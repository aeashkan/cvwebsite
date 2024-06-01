from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Post
from datetime import datetime


def blog_view(request):
    posts = Post.objects.filter(status=1, published_date__lte=datetime.now()).order_by('-published_date')
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)


def single_view(request, pid):
    post = get_object_or_404(Post, pk=pid, status=True, published_date__lte=datetime.now())
    context = {'post': post}
    post.counted_view += 1
    post.save()
    return render(request, 'blog/single.html', context)

from django.shortcuts import render
from django.http import HttpResponse

def blog_view(request):
    return render(request, 'blog/blog.html')

def single_view(request):
    return render(request, 'blog/single.html')
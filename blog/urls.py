from django.urls import path
from blog.views import *
app_name = 'blog'
urlpatterns = [
    path('', blog_view, name='index'),
    path('<int:pid>', single_view, name='single'),
    path('category/<str:cat_name>', blog_view, name='category'),
    path('search/', blog_search, name='search'),
    path('author/<str:author_username>', blog_view, name='author'),
    path('tag/<str:tag_name>', blog_view, name='tag')
]
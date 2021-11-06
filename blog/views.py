from django.shortcuts import render
from .models import Blog


def all_blogs(request):
    blog = Blog.objects.all()
    count = blog.count()
    return render(request, 'blog/all_blogs.html', {'blogs': blog, 'blogs_count': count})
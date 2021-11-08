from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs(request):
    blog_obj = Blog.objects.all()
    count = blog_obj.count()
    return render(request, 'blog/all_blogs.html', {'blogs': blog_obj, 'blogs_count': count})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})


from django.shortcuts import render
from .models import Post


def main_page(request):
    posts = Post.objects.filter(is_public=True).order_by('-id').all()
    context = {'title': 'Привет МИР!', 'posts': posts}
    return render(request, 'mainpage.html', context)

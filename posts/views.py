from django.shortcuts import render
from .models import *
# Create your views here.


def posts(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'posts/posts.html', context)


def hashtags(request):
    context = {
        'hashtags': Hashtag.objects.all()
    }
    return render(request, 'hashtags/hastags.html', context)
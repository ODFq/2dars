from multiprocessing import context
from django.shortcuts import render
from .models import Post
# Create your views here.

def home(request):
   posts = Post.objects.all()
   context = {
        'posts':posts}
   return render(request, 'index.html',context)


def example(request):
    posts = Post.objects.all()
    context = {
        'posts':posts

    }
    return render(request, 'examp.html',context)
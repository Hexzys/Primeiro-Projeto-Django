from re import U
from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import *
# Create your views here.
def home(request):
    #load aal the post from db(10)
    posts =Post.objects.all()[:11]
    #print(posts)
    cats=Category.objects.all()
    data={
        'posts':posts,
        'cats':cats,
    }
    return render (request,'home.html',data)

def post(request,url):
    post=Post.objects.get(url=url)
    cats=Category.objects.all()
    data={
        'post':post,
        'cats':cats,
    }
    # print(post)
    return render(request,'posts.html',data)

def category(request,url):
    cat=Category.objects.get(url=url)
    posts=Post.objects.filter(cat=cat)
    data={
        'cat':cat,
        'posts':posts
    }
    return render (request,'category.html',data)
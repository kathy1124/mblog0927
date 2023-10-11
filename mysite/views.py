from django.shortcuts import render
from mysite.models import Post
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request ,'index.html', locals())

def showpost(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request ,'post.html', locals())

'''
def homepage(request):
    posts = Post.objects.all() #select * from post
    post_lists = list()
    for counter,post in enumerate(posts):#enumerate  -> 回傳(index,data)(索引詞,資料)
        post_lists.append(f'No. {counter}-{post} <br>') #{}包變數 <br>換行
    return HttpResponse(post_lists)
'''

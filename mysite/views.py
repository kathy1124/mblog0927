from django.shortcuts import render
from mysite.models import Post
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect

# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request ,'index.html', locals())
                #把 urls.py 的變數傳進來0
def showpost(request, slug): # <-
    try: 
        post = Post.objects.get(slug=slug)
        if post != None:
            return render(request ,'post.html', locals())
        else: #如果網址錯誤->導到首頁
            return redirect("/")
    except:
        return redirect("/")
    # select * from post where slug=%slug
'''
def homepage(request):
    posts = Post.objects.all() #select * from post
    post_lists = list()
    for counter,post in enumerate(posts):#enumerate  -> 回傳(index,data)(索引詞,資料)
        post_lists.append(f'No. {counter}-{post} <br>') #{}包變數 <br>換行
    return HttpResponse(post_lists)
'''

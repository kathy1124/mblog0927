from mytest.models import Post, Mood
from django.shortcuts import redirect, render
# Create your views here.
def index(request):
    posts = Post.objects.filter(enabled=True).order_by('-pub_time')[:30] #用pub_time倒序 顯示前3筆
    moods= Mood.objects.all()
    if request.method == 'GET':
        return render(request, 'myform.html', locals())
    elif request.method == 'POST':
        try:
            user_id = request.POST['user_id']
            user_pass = request.POST['user_pass']
            user_post = request.POST['user_post']
            user_mood = request.POST['mood']
            mood = Mood.objects.get(status=user_mood)
            post = Post(mood=mood, nickname=user_id, del_pass=user_post, message=user_post )
            post.save()
            message = f'成功儲存！請儲存你的編輯密碼[{user_pass}]!，訊息需審查後才會顯示'.format(user_pass)
            return render(request,"myform.html",locals())
        except Exception as e:
            print(e)
            message = '出現錯誤'
            return render(request, 'myform.html', locals())
    else:
        message ='/post/get 出現錯誤'
        return render(request, 'myform.html', locals())
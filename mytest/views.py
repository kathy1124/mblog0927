from django.shortcuts import render
from mytest.models import Post, Mood, Profile
from django.shortcuts import redirect
from mytest.forms import ContactForm , UserRegisterForm,LoginForm, ProfileForm
# PostForm
def index(request): 
    posts = Post.objects.filter(enabled=True).order_by('-pub_time')[:30]#[:30]取前三十個,日期排序
    moods = Mood.objects.all()#把東西從資料庫抓出來
    if request.method == 'GET':
        return render(request,'myform.html',locals())
    elif request.method =='POST':
        try:
            user_id = request.POST['user_id']
            user_pass = request.POST['user_pass']
            user_post = request.POST['user_post']
            user_mood = request.POST['mood']
            mood = Mood.objects.get(status=user_mood)
            post = Post(moods=mood, nickname=user_id, del_pass=user_pass, message=user_post)#先把物件綁定到post裡面
            post.save()
            message = '成功儲存！請記得你的編輯密碼[{}]!，訊息需經審查後才會顯示。'.format(user_pass)
            return render(request,'myform.html',locals())
        except Exception as e:
            print(e)
            message = '出現錯誤'
            return render(request,'myform.html',locals())
    else:
            message = 'post/get 出現錯誤'
            return render(request,'myform.html',locals())
    
def delpost(request,pid):
    if pid:
        try:
            post = Post.objects.get(id=pid)
            post.delete()
        except:
            print('刪除錯誤!! pid=',pid)
            pass
    return redirect("/")

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request, 'myContact.html',locals()) 
    elif request.method == 'POST':
        form = ContactForm(request.POST)#抓資料
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            user_message = form.cleaned_data['user_message']
            print('user_name:',user_name)
            print('user_message:',user_message)
        return render(request, 'myContact.html', locals())
    else:
        message = "ERROR"
        return render(request, 'myContact.html', locals())
    
# def post2db(request):
#     if request.method == 'GET':
#         form = PostForm()
#         return render(request, 'myPost2DB.html', locals())
#     elif request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return render(request, 'myPost2DB.html', locals())
#     else:
#         message = "ERROR"
#         return render(request, 'myPost2DB.html', locals())


#1227
from django.contrib.auth.models import User

def register(request):
    if request.method == 'GET':
        form = UserRegisterForm()
        return render(request, 'register.html', locals())
    elif request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            user_email = form.cleaned_data['user_email']
            user_password = form.cleaned_data['user_password']
            user_password_confirm = form.cleaned_data['user_password_confirm']
            if user_password == user_password_confirm:
                user = User.objects.create_user(user_name, user_email, user_password)
                message = f'註冊成功！'
            else:
                message = f'兩次密碼不一致！'    
        return render(request, 'register.html', locals())
    else:
        message = "ERROR"
        return render(request, 'register.html', locals())
    
from django.contrib.auth import authenticate
from django.contrib import auth

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', locals())
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            user_password = form.cleaned_data['user_password']
            user = authenticate(username=user_name, password=user_password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    print("success")
                    message = '成功登入了'
                    return redirect('/')
                else:
                    message = '帳號尚未啟用'
            else:
                 message = '登入失敗'
        return render(request, 'login.html', locals())
    else:
        message = "ERROR"
        return render(request, 'login.html', locals())
    
# @login_required(login_url='/login/') 
def profile(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            username = request.user.username
            try:
                user = User.objects.get(username=username)
                userinfo = Profile.objects.get(user=user)
                form = ProfileForm(userinfo)
            except:
                form = ProfileForm()
        return render(request, 'userinfo.html', locals())
    elif request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProfileForm()
            message = f'成功儲存！請記得你的編輯密碼!，訊息需經審查後才會顯示。'
        return render(request, 'userinfo.html', locals())
    else:
        message = "ERROR"
        print('出錯回首頁')
        redirect("/")
from django.shortcuts import render
from mysite.models import Post
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect

# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    hour = now.timetuple().tm_hour
    # print(f'hour = {hour}')
    return render(request ,'index.html', locals())
                #把 urls.py 的變數傳進來0   locals() = {posts:posts, now,now}
                
def showpost(request, slug): # <-
    # try: 
    post = Post.objects.get(slug=slug)
        # if post != None:
    return render(request ,'post.html', locals())
    #     else: #如果網址錯誤->導到首頁
    #         return redirect("/")
    # except:
    #     return redirect("/")
    # select * from post where slug=%slug
    
import random  #random 隨機
def about(request, num=-1):
    quotes = ['今日，今日畢',
              '要怎麼收穫先那麼栽',
              '知識就是力量',
              '一個人的個性就是他的命運']
    if num == -1 or num >4:
        quote = random.choice(quotes)
    else:
        quote = quote[num]
    return render(request, 'about.html',locals())  

# def carlist(request, maker=0):
#     car_maker = ['SAAB', 'Ford', 'Honda', 'Mazda', 'Nissan','Toyota' ]
#     car_list = [ 
#                 [],
#                 ['Fiesta', 'Focus', 'Modeo', 'EcoSport', 'Kuga', 'Mustang'],
#                 ['Fit', 'Odyssey', 'CR-V', 'City', 'NSX'],
#                 ['Mazda3', 'Mazda5', 'Mazda6', 'CX-3', 'CX-5', 'MX-5'],
#                 ['Tida', 'March', 'Livina', 'Sentra', 'Teana', 'X-Trail', 'Juke', 'Murano'],
#                 ['Camry','Altis','Yaris','86','Prius','Vios', 'RAV4', 'Wish']
# 	            ]
#     maker = maker
#     maker_name =  car_maker[maker]
#     cars = car_list[maker]
#     return render(request, 'carlist.html', locals())

def carlist(request, maker=0):
    car_maker = ['Ford', 'Honda', 'Mazda']
    car_list = [
        [{'model':'Fiesta', 'price': 203500},
            {'model':'Focus','price': 605000},
            {'model':'Mustang','price': 900000}],
        [{'model':'Fit', 'price': 450000}, 
            {'model':'City', 'price': 150000}, 
            {'model':'NSX', 'price':1200000}],
		[{'model':'Mazda3', 'price': 329999}, 
		    {'model':'Mazda5', 'price': 603000},
		    {'model':'Mazda6', 'price':850000}],]
    maker = maker
    maker_name =  car_maker[maker]
    cars = car_list[maker]
    return render(request, 'carlist.html', locals())



'''
def homepage(request):
    posts = Post.objects.all() #select * from post
    post_lists = list()
    for counter,post in enumerate(posts):#enumerate  -> 回傳(index,data)(索引詞,資料)
        post_lists.append(f'No. {counter}-{post} <br>') #{}包變數 <br>換行
    return HttpResponse(post_lists)
'''
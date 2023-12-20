"""
URL configuration for mblog0927 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# **** 搭配views.py ****
from django.contrib import admin
from django.urls import path
# from mysite.views import homepage  
from mysite import views as mv
from mytest import views as testv

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',homepage) #什麼都沒輸入'預設'到homepage
    path('',mv.homepage, name="homepage"),
    path('post/<slug:slug>/', mv.showpost, name="showpost"), #<變數> #<資料型態:變數>
    path('post/', mv.show_all_post, name="show-all-post"), #看留言
    path('post/<int:post_id>/comments', mv.show_comments, name='show-comments'), #post唯一的postid show出comments
    path('about/',mv.about),
    path('about/<int:num>',mv.about, {'num':1}),
    path('post/<int:yr>/<int:mon>/<int:day>/<int:post_num>',mv.Post, name='post-url' ),
    path('carlist/', mv.carlist, name='carlist'), #path('網址',函式)
    path('carlist/<int:maker>/', mv.carlist, name='carlist-url'),
    path('post/new', mv.new_post, name='post-new'),
    path('test',mv.homepage,name='test-name'),
    path('test/new',testv.index,name='test-name'),
]         

from django.contrib import admin
from mysite.models import Post, Product, Comment #定義的post納入管理
from mysite.models import Product

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')  #文章顯示時有 title、slug、pub_date(標題、網址、日期)
admin.site.register(Post, PostAdmin)

admin.site.register(Product)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'pub_date') 
admin.site.register(Comment, CommentAdmin)


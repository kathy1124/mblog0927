from django.contrib import admin
from mysite.models import Post   #定義的post納入管理
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')
admin.site.register(Post, PostAdmin)

from django.contrib import admin
from mysite.models import post   #定義的post納入管理
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')
admin.site.register(post, PostAdmin)

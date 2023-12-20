from django.contrib import admin
from mytest.models import Post, Mood
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'message', 'del_pass', 'pub_time', 'enabled')
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'pub_date')
    
admin.site.register(Post, PostAdmin)
admin.site.register(Mood)
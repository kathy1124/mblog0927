from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200) #標題
    slug = models.CharField(max_length=200)  #標題
    body = models.TextField()                #長文字(內文)
    pub_date = models.DateTimeField(auto_now_add=True) #時間
     
    class Meta:      #'-'反向排序
         ordering = ('-pub_date', ) #排序大到小
     
    def __str__(self) -> str:  #python內建
        return self.title
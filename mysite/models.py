from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200) #標題
    slug = models.CharField(max_length=200)  #連結
    body = models.TextField()                #長文字(內文)
    pub_date = models.DateTimeField(auto_now_add=True) #本文發表的時間
                                    #資料庫在建立時自動加入當時的時間
    class Meta:      #'-'反向排序
        ordering = ('-pub_date', ) #排序大到小
    
    def __str__(self) -> str:  #python內建-
        return self.title   #產生項目資料時以文章標題的內容為代表


class Comment(models.Model):
    post = models.ForeignKey(Post ,on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text

class Product(models.Model):
    SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    sku = models.CharField(max_length=5)
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    size = models.CharField(max_length=1, choices=SIZES)


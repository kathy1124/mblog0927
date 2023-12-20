from django import forms
from mytest import models
from mytest.models import Post

class ContactForm(forms.Form):
    CITY = [
        ['TP', 'Taipei'],   #['程式抓得值','user看到的']
        ['TY', 'Taoyuang'],
        ['TC', 'Taichung'],
        ['TN', 'Tainan'],
        ['KS', 'Kaohsiung'],
        ['NA', 'Others'],
    ]                                                           #預設值
    user_name = forms.CharField(label='您的姓名', max_length=50, initial='李大仁')
    user_city = forms.ChoiceField(label='居住城市', choices=CITY) # ChoiceField ->下拉式選單
    user_school = forms.BooleanField(label='是否在學', required=False)
    user_email = forms.EmailField(label='電子郵件')  
    user_message = forms.CharField(label='您的意見', widget=forms.Textarea)  #widget=forms.Textarea -> 擴增成為大量文字輸入欄位，亦即<textarea>標籤。


class PostForms(forms.MODELForm):
    class Meta:
        model = Post 
        fields = ['moods','nickname', 'message' , 'del_pass']
    
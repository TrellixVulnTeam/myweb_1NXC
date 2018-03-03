# -*- coding=utf-8 -*-
__author__ = 'zhaojie'
__date__ = '2018/2/23 16:54'
import re
from django import forms
from operation.models import UserAsk
# class UserAskForm(forms.Form):
#     name = forms.CharField(required=True, min_length=2, max_length=20)
#     phone = forms.CharField(required=True, min_length= 11)
#     course_name = forms.CharField(required=True, min_length=1, max_length=50)

# 上面的form和model几乎一样，django采用modelform避免这种情况
class UserAskForm(forms.ModelForm):

    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self): # 自定义验证函数，必须clean开头
        '''
        验证手机号码是否合法
        '''
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = '^1[358]\d{9}$|^147\d{8}$|^176\d{8}$'
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u'手机号码非法', code='mobile_invalid')
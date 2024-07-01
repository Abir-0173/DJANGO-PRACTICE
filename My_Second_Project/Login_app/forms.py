# from django.db import forms
from django import forms
from django.contrib.auth.models import User
from Login_app.models import UserInfo

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserInfoForm(forms.ModelForm):
    class Meta():
        model = UserInfo
        fields = ('facebook_id', 'profile_pics')
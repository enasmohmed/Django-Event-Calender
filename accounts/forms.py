from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from accounts import models
from accounts.models import Profile

User = get_user_model()


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields= ['username','first_name','last_name','email']



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city','phone_number','image']
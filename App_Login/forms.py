from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import UserProfile


class CreteNewUser(UserCreationForm):
    email = forms.EmailField(label='', required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Enter Your Email'}))
    phone_number = forms.CharField(label='',
                                   widget=forms.TextInput(
                                       attrs={'placeholder': 'Enter Your Mobile Number (+)country code +8801723283638'}))
    username = forms.CharField(label="", widget=forms.TextInput(attrs=({'placeholder': 'Enter your username'})))
    password1 = forms.CharField(required=True, label='',
                                widget=forms.PasswordInput(attrs=({'placeholder': "Password"})))
    password2 = forms.CharField(required=True, label='',
                                widget=forms.PasswordInput(attrs=({'placeholder': 'Confirm Password'})))

    class Meta:
        model = User
        fields = ('email', 'username', 'phone_number', 'password1', 'password2')


class EditProfile(forms.ModelForm):
    dob = forms.DateField(label='Date Of Birth', widget=forms.TextInput(attrs={'type': 'date'}))
    fullname = forms.CharField(label='Full Name')

    class Meta:
        model = UserProfile
        exclude = ('user',)
        fields = ('profile_pic', 'fullname', 'description', 'dob', 'website', 'facebook')
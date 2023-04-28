from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email']

    
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']
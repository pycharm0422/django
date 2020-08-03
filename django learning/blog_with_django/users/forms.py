from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


# class UserUpdateForm(UserCreationForm):
#     class Meta:
#         modal = User
#         fields = ['username', 'email']

# class UserProfileForm(UserCreationForm):
#     image = forms.ImageField()

#     class Meta:
#         modal = User
#         fields = ['image']
        
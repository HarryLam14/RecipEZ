from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    favourite_ingredient = forms.CharField(max_length = 50)

    class Meta:
        model = User
        fields = ['username', 'favourite_ingredient', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    favourite_ingredient = forms.CharField(max_length = 50)

    class Meta:
        model = User
        fields = ['username', 'favourite_ingredient']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
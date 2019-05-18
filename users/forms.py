from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# New form to have additional field - Email
# Inherit from django's UserCreationForm
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField() # Default Required

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Allows us to Update 'username', 'email'
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


# Allows us to Update 'image'
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
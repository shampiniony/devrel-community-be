from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'middle_name', 'sex', 'birth_date', 'bio', 'avatar')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'middle_name', 'sex', 'birth_date', 'bio', 'avatar')

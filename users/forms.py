from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import ModelForm
from .models import Profile

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', "email", "first_name", "last_name"]


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["picture", "bio", "anonym"]

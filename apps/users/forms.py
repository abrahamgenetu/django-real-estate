import imp
from pyexpat import model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User



class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ["email","username","first_name","last_name"]
        error_class = "error"


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserCreationForm):
        model = User
        fields = ["email","username","first_name","last_name"]
        error_class = "error"
        
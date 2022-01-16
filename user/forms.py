from django.contrib.auth.forms import UserCreationForm

from user.models import CustomUser


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['username', 'full_name', 'password1', 'password2', 'email']

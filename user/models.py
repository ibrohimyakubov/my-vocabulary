from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser):
    full_name = models.CharField('full name', max_length=200, blank=True, null=True)
    email = models.EmailField('email address', blank=False, null=False, unique=True)
    date_joined = models.DateTimeField('date joined', default=timezone.now)
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        'username',
        max_length=150,
        unique=True,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[username_validator],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )

    def get_departments(self):
        return self.bigdepartment_set.all()

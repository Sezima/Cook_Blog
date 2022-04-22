from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

# кастомный юзер
class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='users')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

'''
in AbstractUser have 
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"  это означает что регистрация будет по юзернейму
    REQUIRED_FIELDS = ["email"]
'''

# метод который отвечает за отаброжение

def __str__(self):
    return self.get_full_name()

# method get_full_name() взят из абстрактюзера кторый конкатенирует имя и фамилию

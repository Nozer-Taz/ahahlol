from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class Group(models.Model):
    group_name = models.CharField(max_length=255)

    def __str__(self):
        return self.group_name


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email is not provided!')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.is_staff = False
        user.is_superuser = False
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email is not provided!')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    overall_points = models.IntegerField(blank=True, null=True)
    rating_place = models.IntegerField(blank=True, null=True)
    tests_taken = models.IntegerField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email



#AbstractBaseUser -> для создания модели пользователя с нуля самостоятельно
#AbstractUser -> для создания модели по уже предложенному шаблону, чаще всего меняется, чтобы убрать username
#BaseUserManager -> тоже меняется, при использовании AbstractUser, нужно прописать что вместо username используется email в качестве уникального идентификатора

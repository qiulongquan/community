from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)

from .manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Model to create users.
    """
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)

    is_admin = models.BooleanField(default=False)       # 如果用户具有所有权限，值为True。
    is_superuser = models.BooleanField(default=False)   # 如果用户具有所有权限，值为True。
    is_staff = models.BooleanField(default=False)       # 如果用户被允许访问管理界面，值为 True。
    is_active = models.BooleanField(default=True)       # 如果用户帐户当前处于活动状态，值为True。

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]


    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


    def get_userid(self):
        return User.objects.get(username=self.username).user_id
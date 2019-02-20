from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, username, email, password, **kwargs):
        """
        Create a authentication.
        :param username:
        :param email:
        :param password:
        :param kwargs:
        :return:
        """
        if not email:
            raise ValueError("Users must have avalid email address.")

        user = self.model(
            username = username,
            email = self.normalize_email(email),
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password, **kwargs):
        """
        Create a super authentication.
        :param username:
        :param email:
        :param password:
        :param kwargs:
        :return:
        """
        user = self.create_user(
            username, email, password, **kwargs
        )

        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
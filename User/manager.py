from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, username, role, password, **extra_fields):
        """
        Create and save a User with the username,role and password
        :param email:
        :param role:
        :param username:
        :param password:
        :param extra_fields:
        :return:
        """
        if not username and not role:
            raise ValueError(_('The Username and the role must be set'))
        user = self.model(username=username, role=role, **extra_fields)
        user.set_password(password)
        user.save()
        return user
        # Create and save a SuperUser with the given username nad password

    def create_superuser(self, username, password, **extra_fields):
        """
        Create and save a SuperUser with the given username and password
        :param username:
        :param password:
        :param extra_fields:
        :return:
        """

        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 'Admin')
        extra_fields.setdefault('is_admin', 'True')
        extra_fields.setdefault('is_staff', 'True')

        user = self.create_user(username=username, password=password, **extra_fields)
        return user

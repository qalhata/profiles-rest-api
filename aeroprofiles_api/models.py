from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """ Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """ Create a new user profile"""
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """ Create and save new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

# We create a new class called user profile
# which inherits from the abstract base user and
# permissionmixin base classes

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database Model for users in the system"""
    """ Now we define the fields"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)

    """ we add fields for status of the user profile"""
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    """ we specify the model manager we will use"""
    """ for the objects - since we wil be using our custom model with"""
    """ our django CLI"""

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """ Retrieve short name of user"""
        return self.name

    """ we specify the string representation of our model"""
    """ This is the item we want to return when we concert"""
    """ a user profile object to a string"""

    def __str__(self):
        """Return string representation of our user model"""
        return self.email


# Create your models here.

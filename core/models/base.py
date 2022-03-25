import uuid
from datetime import datetime

from django.db import models
from django.db.models import QuerySet
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager


class UserProfileManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    id = models.CharField(primary_key=True, max_length=36, editable=False, default=uuid.uuid4)
    username = None
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    profile_image = models.ImageField(upload_to='avatars/', null=True, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    country = models.ForeignKey("core.Country", on_delete=models.SET_NULL, null=True, blank=True)
    state = models.ForeignKey("State", on_delete=models.SET_NULL, null=True, blank=True)
    city = models.ForeignKey("City", on_delete=models.CASCADE, null=True, blank=True)
    about = models.TextField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserProfileManager()

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    # def __str__(self):
    #     if self.first_name and self.last_name:
    #         return str(self.first_name + " " + self.last_name)
    #     return self.email


class SoftDeletionQuerySet(QuerySet):
    def delete(self):
        return super(SoftDeletionQuerySet, self).update(deleted_at=datetime.now())

    def hard_delete(self):
        return super(SoftDeletionQuerySet, self).delete()

    def alive(self):
        return self.filter(deleted_at=None)

    def dead(self):
        return self.exclude(deleted_at=None)


class SoftDeletionManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super(SoftDeletionManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        if self.alive_only:
            return SoftDeletionQuerySet(self.model).filter(deleted_at=None)
        return SoftDeletionQuerySet(self.model)

    def hard_delete(self):
        return self.get_queryset().hard_delete()


class Base(models.Model):
    status = models.BooleanField(default=True)

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='%(class)s_createdby',
        db_column='created_by',
        null=True
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='%(class)s_updated_by',
        db_column='updated_by',
        null=True
    )
    deleted_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='%(class)s_deleted_by',
        db_column='deleted_by',
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)

    class Meta:
        abstract = True

    def delete(self, **kwargs):
        self.deleted_at = datetime.now()
        self.save()

    def hard_delete(self):
        super(Base, self).delete()

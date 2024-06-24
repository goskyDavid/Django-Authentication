import datetime
import hashlib

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone

from account.constants import Gender, UserRoles


class CustomUserManager(BaseUserManager):
    @property
    def random_password(self):
        p = hashlib.sha256()
        now = datetime.datetime.utcnow()
        new_pass = (now.strftime("%Y%m%d%H%M%S%f")).encode("utf-8")
        p.update(new_pass)
        password = str(p.hexdigest()[:6])
        return password

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        first_name = extra_fields["name"].strip().upper() if extra_fields.get("name") else ""

        user = self.model(
            email=email,
            first_name=first_name,
            is_active=True,
        )

        if password is None:
            password = self.random_password

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        u = self.create_user(email, password, **extra_fields)
        u.is_active = True
        u.is_staff = True
        u.is_superuser = True
        u.save(using=self._db)
        return u

    def set_password(self, user):
        password = self.random_password
        user.set_password(password)
        user.save()
        return password

    def undeleted(self):
        return self.filter(deleted=False)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=511, unique=True, primary_key=True, db_index=True, verbose_name="Email")

    phone = models.CharField(max_length=63, null=True, blank=True, verbose_name="Phone", db_index=True)
    rut = models.CharField(max_length=31, null=True, blank=True, verbose_name="RUT", db_index=True)
    first_name = models.CharField(max_length=511, null=True, blank=True, verbose_name="First name", db_index=True)
    last_name = models.CharField(max_length=511, null=True, blank=True, verbose_name="Last name", db_index=True)
    birthday = models.DateField(null=True, blank=True, verbose_name="Birthday")
    picture = models.CharField(max_length=1023, null=True, blank=True, verbose_name="Avatar")
    gender = models.IntegerField(default=Gender.UNKNOWN.value, verbose_name="Gender", choices=Gender.choices())

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    is_staff = models.BooleanField(default=False, verbose_name="Is staff")
    is_active = models.BooleanField(default=False, verbose_name="Is active")
    email_verified_at = models.DateTimeField(null=True, blank=True, verbose_name="Email verified at")
    role = models.CharField(max_length=31, default=UserRoles.UPDATER.value, verbose_name="Role")

    deleted = models.BooleanField(default=False, verbose_name="Deleted")
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name="Deleted at")

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"

    class Meta:
        db_table = "users"

    def __str__(self) -> str:
        return self.email

    def delete(self, kwargs):
        raise NotImplementedError("Eliminar esta instancia de modelo no está permitido, use `soft_delete()`")

    def soft_delete(self) -> None:
        if not self.deleted:
            self.deleted = True
            self.deleted_at = timezone.now()
            super().save(
                update_fields=(
                    "deleted",
                    "deleted_at",
                )
            )

    @property
    def user_name(self) -> str:
        un = ""
        if self.first_name:
            un = self.first_name
        if self.last_name:
            un += f" {self.last_login}" if un else self.last_name
        if un:
            return un
        return self.email

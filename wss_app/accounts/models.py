from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import models as auth_models
from django.utils.translation import gettext_lazy as _

from wss_app.accounts.managers import WssUserManager
from wss_app.accounts.validators import validate_picture_file_size


class WssUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    is_staff = models.BooleanField(
        default=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    USERNAME_FIELD = "email"

    objects = WssUserManager()


class Profile(models.Model):
    MAX_LENGTH_NAME = 40

    first_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        null=True,
        blank=True,
    )

    profile_picture = models.ImageField(
        upload_to='profile_pictures',
        validators=(validate_picture_file_size,),
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        WssUser,
        primary_key=True,
        on_delete=models.CASCADE,
        related_name='profile',
    )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'

        return self.first_name or self.last_name


# class AccountReview(models.Model):
#     review = models.TextField()
#
#     rating = models.PositiveIntegerField(default=0)
#
#     created_at = models.DateTimeField()
#
#     reviewer = models.ForeignKey(
#         Profile,
#         on_delete=models.CASCADE
#     )
#
#     def save(self, *args, **kwargs):
#         if not self.created_at:
#             self.created_at = timezone.now()
#         return super(AccountReview, self).save(*args, **kwargs)

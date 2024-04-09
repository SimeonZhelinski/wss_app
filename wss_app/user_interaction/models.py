from django.core import validators
from django.db import models

from wss_app.accounts.models import WssUser


class ContactMessage(models.Model):
    MAX_LENGTH_NAME = 100

    user = models.ForeignKey(
        WssUser,
        on_delete=models.CASCADE
    )

    subject = models.CharField(
        null=False,
        blank=False,
    )

    message = models.TextField(
        null=False,
        blank=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )


class Review(models.Model):
    RATING_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    ]
    MIN_LENGTH_COMMENT = 5
    MAX_LENGTH_COMMENT = 200

    user = models.ForeignKey(
        WssUser,
        on_delete=models.CASCADE,
    )

    rating = models.IntegerField(
        choices=RATING_CHOICES,
    )
    comment = models.TextField(
        max_length=MAX_LENGTH_COMMENT,
        validators=(validators.MinLengthValidator(MIN_LENGTH_COMMENT),),
        null=True,
        blank=True
    )

    date_created = models.DateTimeField(
        auto_now=True,
    )

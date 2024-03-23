from django.db import models
from django.utils import timezone


class ContactMessage(models.Model):
    MAX_LENGTH_NAME = 100

    name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        null=False,
        blank=False
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    message = models.TextField(
        null=False,
        blank=False,
    )

    created_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        return super(ContactMessage, self).save(*args, **kwargs)


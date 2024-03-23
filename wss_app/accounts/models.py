from django.db import models
from django.utils import timezone


class Profile(models.Model):
    MAX_LENGTH_NAME = 100

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

    profile_pic = models.ImageField(
        upload_to='media_files'
    )

    password = models.CharField(
        max_length=100
    )

    email = models.EmailField()

    # user = models.OneToOneField(
    #     WssUser,
    #     primary_key=True,
    #     on_delete=models.CASCADE,
    # )


class AccountReview(models.Model):
    review = models.TextField()

    rating = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField()

    reviewer = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        return super(AccountReview, self).save(*args, **kwargs)

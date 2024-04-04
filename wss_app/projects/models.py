from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.text import slugify

from wss_app.accounts.models import Profile, WssUser
from django.core.validators import MinLengthValidator

UserModel = get_user_model()


class ResidentialBuilding(models.Model):
    MAX_LENGTH_NAME = 100
    MIN_LENGTH_NAME = 1

    name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        null=False,
        blank=False,
        validators=[MinLengthValidator(MIN_LENGTH_NAME), ],
    )

    bathroom_sink = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    kitchen_sink = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    toilet_seat = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    washing_machine = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    dishwasher = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    shower = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    bathtub = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    building_residence = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=[MinValueValidator(1), ],
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
        editable=False,
    )

    project_creator = models.ForeignKey(
        WssUser,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.pk}")

        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class BuildingWithoutExistingInfrastructure(ResidentialBuilding):
    pass


class BuildingWithExistingInfrastructure(ResidentialBuilding):
    floor_siphon = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    building_area = models.FloatField(
        validators=[MinValueValidator(1.0), ],
        null=False,
        blank=False,
    )

    property_area = models.FloatField(
        validators=[MinValueValidator(1.0), ],
        null=False,
        blank=False,
    )

    green_area = models.FloatField(
        validators=[MinValueValidator(0.0), ],
        null=False,
        blank=False,
    )

    underground_parking_spots = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    floors = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=[MinValueValidator(1), ],
    )

    def clean(self):
        super().clean()
        if self.building_area + self.green_area > self.property_area:
            raise ValidationError("The sum of the building area and green area cannot exceed the total property area.")


class InfrastructureProject(models.Model):
    MAX_LENGTH_NAME = 100
    MIN_PLUMBING_DEPTH = 1.7
    MAX_PLUMBING_DEPTH = 3
    MIN_SEWER_DEPTH = 2.3
    MAX_SEWER_DEPTH = 5

    PLUMBING_PIPE_DIAMETER_CHOICES = [
        ('DN90', 'DN90'),
        ('DN110', 'DN110'),
        ('DN125', 'DN125'),
        ('DN160', 'DN160'),
        ('DN200', 'DN200'),
        ('DN225', 'DN225'),
        ('DN250', 'DN250'),
        ('DN315', 'DN315'),
        ('DN355', 'DN355'),
        ('DN400', 'DN400'),
    ]

    SEWER_PIPE_DIAMETER_CHOICES = [
        ('DN315', 'DN315'),
        ('DN400', 'DN400'),
        ('DN500', 'DN500'),
        ('DN630', 'DN630'),
        ('DN800', 'DN800'),
        ('DN1000', 'DN1000'),
    ]

    PAVEMENT_CHOICES = [
        ('Asphalt', 'Asphalt'),
        ('Concrete', 'Concrete'),
        ('Stone paving', 'Stone paving'),
        ('Pavers', 'Pavers'),
        ('None', 'None')
    ]
    MIN_LENGTH_NAME = 1

    name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        null=False,
        blank=False,
        validators=[MinLengthValidator(MIN_LENGTH_NAME), ],
    )

    existing_plumbing_depth = models.FloatField(
        validators=[MinValueValidator(MIN_PLUMBING_DEPTH), MaxValueValidator(MAX_PLUMBING_DEPTH)],
        null=False,
        blank=False,
    )

    new_plumbing_length = models.FloatField(
        validators=[MinValueValidator(1.0), ],
        null=False,
        blank=False,
    )

    new_plumbing_diameter = models.CharField(
        choices=PLUMBING_PIPE_DIAMETER_CHOICES,
        null=False,
        blank=False,
    )

    existing_sewer_depth = models.FloatField(
        validators=[MinValueValidator(MIN_SEWER_DEPTH), MaxValueValidator(MAX_SEWER_DEPTH)],
        null=False,
        blank=False,
    )

    new_sewer_length = models.FloatField(
        validators=[MinValueValidator(1.0), ],
        null=False,
        blank=False,
    )

    new_sewer_diameter = models.CharField(
        choices=SEWER_PIPE_DIAMETER_CHOICES,
        null=False,
        blank=False,
    )

    existing_pavement = models.CharField(
        choices=PAVEMENT_CHOICES,
        null=False,
        blank=False,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
        editable=False,
    )

    project_creator = models.ForeignKey(
        WssUser,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.pk}")

        super().save(*args, **kwargs)

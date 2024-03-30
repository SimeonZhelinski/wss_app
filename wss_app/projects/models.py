from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.text import slugify

from wss_app.accounts.models import Profile


class ResidentialBuilding(models.Model):
    MAX_LENGTH_NAME = 100

    name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        null=False,
        blank=False,
    )

    bathroom_sink = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    kitchen_sink = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    toilet_seat = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    washing_machine = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    dishwasher = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    shower = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    bathtub = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    building_residence = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    floor_siphon = models.PositiveIntegerField(
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
        Profile,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.pk}")

        super().save(*args, **kwargs)

    def clean(self):
        super().clean()
        if all(field <= 0 for field in [
            self.bathroom_sink,
            self.kitchen_sink,
            self.toilet_seat,
            self.washing_machine,
            self.dishwasher,
            self.shower,
            self.bathtub,
        ]):
            raise ValidationError("You must have at least one Sanitary from the listed")

    class Meta:
        abstract = True


class BuildingWithoutExistingInfrastructure(ResidentialBuilding):
    pass


class BuildingWithExistingInfrastructure(ResidentialBuilding):
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

    floors = models.PositiveIntegerField()

    def clean(self):
        super().clean()
        if self.building_area > self.property_area:
            raise ValidationError("Building area cannot be greater than property area")


class InfrastructureProject(models.Model):
    MAX_LENGTH_NAME = 100
    MIN_PLUMBING_DEPTH = 1.7
    MAX_PLUMBING_DEPTH = 3
    MIN_SEWER_DEPTH = 2.3
    MAX_SEWER_DEPTH = 5

    PLUMBING_PIPE_DIAMETER_CHOICES = [
        ('DN90', 'DN90'),
        ('DN100', 'DN100'),
        ('DN115', 'DN115'),
        ('DN125', 'DN125'),
        ('DN150', 'DN150'),
        ('DN200', 'DN200'),
        ('DN250', 'DN250'),
        ('DN300', 'DN300'),
        ('DN350', 'DN350'),
        ('DN400', 'DN400'),
        ('DN450', 'DN450'),
        ('DN500', 'DN500'),
        ('DN550', 'DN550'),
        ('DN600', 'DN600'),
    ]

    SEWER_PIPE_DIAMETER_CHOICES = [
        ('DN300', 'DN300'),
        ('DN400', 'DN400'),
        ('DN500', 'DN500'),
        ('DN600', 'DN600'),
        ('DN700', 'DN700'),
        ('DN800', 'DN800'),
        ('DN900', 'DN900'),
        ('DN1000', 'DN1000'),
        ('DN1100', 'DN1100'),
        ('DN1200', 'DN1200'),
        ('DN1300', 'DN1300'),
        ('DN1400', 'DN1400'),
        ('DN1500', 'DN1500'),
        ('DN1600', 'DN1600'),
        ('DN1700', 'DN1700'),
        ('DN1800', 'DN1800'),
        ('DN1900', 'DN1900'),
        ('DN2000', 'DN2000'),
        ('DN2100', 'DN2100'),
        ('DN2200', 'DN2200'),
    ]

    PAVEMENT_CHOICES = [
        ('Asphalt', 'Asphalt'),
        ('Concrete', 'Concrete'),
        ('Stone paving', 'Stone paving'),
        ('Pavers', 'Pavers'),
    ]

    name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        null=False,
        blank=False,
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
        Profile,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.pk}")

        super().save(*args, **kwargs)

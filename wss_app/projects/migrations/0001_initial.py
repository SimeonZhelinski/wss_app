# Generated by Django 5.0.3 on 2024-04-02 09:14

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BuildingWithExistingInfrastructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(1)])),
                ('bathroom_sink', models.PositiveIntegerField(blank=True, null=True)),
                ('kitchen_sink', models.PositiveIntegerField(blank=True, null=True)),
                ('toilet_seat', models.PositiveIntegerField(blank=True, null=True)),
                ('washing_machine', models.PositiveIntegerField(blank=True, null=True)),
                ('dishwasher', models.PositiveIntegerField(blank=True, null=True)),
                ('shower', models.PositiveIntegerField(blank=True, null=True)),
                ('bathtub', models.PositiveIntegerField(blank=True, null=True)),
                ('building_residence', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('floor_siphon', models.PositiveIntegerField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('building_area', models.FloatField(validators=[django.core.validators.MinValueValidator(1.0)])),
                ('property_area', models.FloatField(validators=[django.core.validators.MinValueValidator(1.0)])),
                ('green_area', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('underground_parking_spots', models.PositiveIntegerField()),
                ('floors', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('project_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BuildingWithoutExistingInfrastructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(1)])),
                ('bathroom_sink', models.PositiveIntegerField(blank=True, null=True)),
                ('kitchen_sink', models.PositiveIntegerField(blank=True, null=True)),
                ('toilet_seat', models.PositiveIntegerField(blank=True, null=True)),
                ('washing_machine', models.PositiveIntegerField(blank=True, null=True)),
                ('dishwasher', models.PositiveIntegerField(blank=True, null=True)),
                ('shower', models.PositiveIntegerField(blank=True, null=True)),
                ('bathtub', models.PositiveIntegerField(blank=True, null=True)),
                ('building_residence', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('floor_siphon', models.PositiveIntegerField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('project_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InfrastructureProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(1)])),
                ('existing_plumbing_depth', models.FloatField(validators=[django.core.validators.MinValueValidator(1.7), django.core.validators.MaxValueValidator(3)])),
                ('new_plumbing_length', models.FloatField(validators=[django.core.validators.MinValueValidator(1.0)])),
                ('new_plumbing_diameter', models.CharField(choices=[('DN90', 'DN90'), ('DN100', 'DN100'), ('DN115', 'DN115'), ('DN125', 'DN125'), ('DN150', 'DN150'), ('DN200', 'DN200'), ('DN250', 'DN250'), ('DN300', 'DN300'), ('DN350', 'DN350'), ('DN400', 'DN400'), ('DN450', 'DN450'), ('DN500', 'DN500'), ('DN550', 'DN550'), ('DN600', 'DN600')])),
                ('existing_sewer_depth', models.FloatField(validators=[django.core.validators.MinValueValidator(2.3), django.core.validators.MaxValueValidator(5)])),
                ('new_sewer_length', models.FloatField(validators=[django.core.validators.MinValueValidator(1.0)])),
                ('new_sewer_diameter', models.CharField(choices=[('DN300', 'DN300'), ('DN400', 'DN400'), ('DN500', 'DN500'), ('DN600', 'DN600'), ('DN700', 'DN700'), ('DN800', 'DN800'), ('DN900', 'DN900'), ('DN1000', 'DN1000'), ('DN1100', 'DN1100'), ('DN1200', 'DN1200'), ('DN1300', 'DN1300'), ('DN1400', 'DN1400'), ('DN1500', 'DN1500'), ('DN1600', 'DN1600'), ('DN1700', 'DN1700'), ('DN1800', 'DN1800'), ('DN1900', 'DN1900'), ('DN2000', 'DN2000'), ('DN2100', 'DN2100'), ('DN2200', 'DN2200')])),
                ('existing_pavement', models.CharField(choices=[('Asphalt', 'Asphalt'), ('Concrete', 'Concrete'), ('Stone paving', 'Stone paving'), ('Pavers', 'Pavers'), ('None', 'None')])),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('project_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

from django.core.exceptions import ValidationError


def validate_building_area(building_area, property_area):
    if building_area > property_area:
        raise ValidationError("Building area cannot be greater than property area")

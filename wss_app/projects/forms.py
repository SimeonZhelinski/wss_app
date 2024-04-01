from django import forms
from django.core.exceptions import ValidationError

from wss_app.projects.models import BuildingWithExistingInfrastructure, \
    BuildingWithoutExistingInfrastructure, InfrastructureProject


def clean_sanitation_fields(cleaned_data):
    sanitation_fields = [
        'bathroom_sink', 'kitchen_sink', 'toilet_seat',
        'washing_machine', 'dishwasher', 'shower', 'bathtub'
    ]
    if all(cleaned_data.get(field) is None or cleaned_data.get(field) <= 0 for field in sanitation_fields):
        raise ValidationError("You must specify at least one sanitary fixture.")


class BuildingWithoutExistingInfrastructureBaseForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        clean_sanitation_fields(cleaned_data)

    class Meta:
        model = BuildingWithoutExistingInfrastructure
        fields = (
            'name',
            'bathroom_sink',
            'kitchen_sink',
            'toilet_seat',
            'washing_machine',
            'dishwasher',
            'shower',
            'bathtub',
            'building_residence',
            'floor_siphon',
        )

        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Project name", 'required': True}),
            "bathroom_sink": forms.NumberInput(attrs={"placeholder": "Number of bathroom sinks"}),
            "kitchen_sink": forms.NumberInput(attrs={"placeholder": "Number of kitchen sinks"}),
            "toilet_seat": forms.NumberInput(attrs={"placeholder": "Number of toilet seats"}),
            "washing_machine": forms.NumberInput(attrs={"placeholder": "Number of washing machines"}),
            "dishwasher": forms.NumberInput(attrs={"placeholder": "Number of dishwashers"}),
            "shower": forms.NumberInput(attrs={"placeholder": "Number of showers"}),
            "bathtub": forms.NumberInput(attrs={"placeholder": "Number of bathtubs"}),
            "building_residence": forms.NumberInput(
                attrs={"placeholder": "Number of building residences", 'required': True}),
            "floor_siphon": forms.NumberInput(attrs={"placeholder": "Number of floor siphons"}),
        }

        labels = {
            "name": "Project name",
            "bathroom_sink": "Bathroom sink",
            "kitchen_sink": "Kitchen sink",
            "toilet_seat": "Toilet seat",
            "washing_machine": "Washing machine",
            "dishwasher": "Dishwasher",
            "shower": "Shower",
            "bathtub": "Bathtub",
            "building_residence": "Building residences",
            "floor_siphon": "Floor siphon",

        }


class BuildingWithoutExistingInfrastructureCreateForm(BuildingWithoutExistingInfrastructureBaseForm):
    pass


class BuildingWithoutExistingInfrastructureEditForm(BuildingWithoutExistingInfrastructureBaseForm):
    pass


class BuildingWithoutExistingInfrastructureDeleteForm(BuildingWithoutExistingInfrastructureBaseForm):
    pass


class BuildingWithExistingInfrastructureBaseForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        clean_sanitation_fields(cleaned_data)

    class Meta:
        model = BuildingWithExistingInfrastructure
        fields = (
            'name',
            'bathroom_sink',
            'kitchen_sink',
            'toilet_seat',
            'washing_machine',
            'dishwasher',
            'shower',
            'bathtub',
            'building_residence',
            'floor_siphon',
            'building_area',
            'property_area',
            'green_area',
            'underground_parking_spots',
            'floors'
        )

        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Project name", 'required': True}),
            "bathroom_sink": forms.NumberInput(attrs={"placeholder": "Number of bathroom sinks"}),
            "kitchen_sink": forms.NumberInput(attrs={"placeholder": "Number of kitchen sinks"}),
            "toilet_seat": forms.NumberInput(attrs={"placeholder": "Number of toilet seats"}),
            "washing_machine": forms.NumberInput(attrs={"placeholder": "Number of washing machines"}),
            "dishwasher": forms.NumberInput(attrs={"placeholder": "Number of dishwashers"}),
            "shower": forms.NumberInput(attrs={"placeholder": "Number of showers"}),
            "bathtub": forms.NumberInput(attrs={"placeholder": "Number of bathtubs"}),
            "building_residence": forms.NumberInput(
                attrs={"placeholder": "Number of building residences", 'required': True}),
            "floor_siphon": forms.NumberInput(attrs={"placeholder": "Number of floor siphons"}),
            "building_area": forms.NumberInput(attrs={"placeholder": "Building area", 'required': True}),
            "property_area": forms.NumberInput(attrs={"placeholder": "Property area", 'required': True}),
            "green_area": forms.NumberInput(attrs={"placeholder": "Green area in the property", 'required': True}),
            "underground_parking_spots": forms.NumberInput(
                attrs={"placeholder": "Number of underground parking spots", 'required': True}),
            "floors": forms.NumberInput(attrs={"placeholder": "Number of building floors", 'required': True}),
        }

        labels = {
            "name": "Project name",
            "bathroom_sink": "Bathroom sink",
            "kitchen_sink": "Kitchen sink",
            "toilet_seat": "Toilet seat",
            "washing_machine": "Washing machine",
            "dishwasher": "Dishwasher",
            "shower": "Shower",
            "bathtub": "Bathtub",
            "building_residence": "Building residences",
            "floor_siphon": "Floor siphon",
            "building_area": "Building area",
            "property_area": "Property area",
            "green_area": "Green area",
            "underground_parking_spots": "Underground parking spots",
            "floors": "Floors",
        }


class BuildingWithExistingInfrastructureCreateForm(BuildingWithExistingInfrastructureBaseForm):
    pass


class BuildingWithExistingInfrastructureEditForm(BuildingWithExistingInfrastructureBaseForm):
    pass


class BuildingWithExistingInfrastructureDeleteForm(BuildingWithExistingInfrastructureBaseForm):
    pass


class InfrastructureProjectBaseForm(forms.ModelForm):
    class Meta:
        model = InfrastructureProject
        fields = (
            'name',
            'existing_plumbing_depth',
            'new_plumbing_length',
            'new_plumbing_diameter',
            'existing_sewer_depth',
            'new_sewer_length',
            'new_sewer_diameter',
            'existing_pavement',
        )

        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Project name", 'required': True}),
            "existing_plumbing_depth": forms.NumberInput(attrs={"placeholder": "Existing plumbing depth", 'required': True}),
            "new_plumbing_length": forms.NumberInput(attrs={"placeholder": "New plumbing length", 'required': True}),
            "new_plumbing_diameter": forms.Select(attrs={"placeholder": "New plumbing diameter", 'required': True}),
            "existing_sewer_depth": forms.NumberInput(attrs={"placeholder": "Existing sewer depth", 'required': True}),
            "new_sewer_length": forms.NumberInput(attrs={"placeholder": "New sewer length", 'required': True}),
            "new_sewer_diameter": forms.Select(attrs={"placeholder": "New sewer diameter", 'required': True}),
            "existing_pavement": forms.Select(attrs={"placeholder": "Existing pavement", 'required': True}),
        }

        labels = {
            "name": "Project name",
            "existing_plumbing_depth": "Existing plumbing depth",
            "new_plumbing_length": "New plumbing length",
            "new_plumbing_diameter": "New plumbing diameter",
            "existing_sewer_depth": "Existing sewer depth",
            "new_sewer_length": "New sewer length",
            "new_sewer_diameter": "New sewer diameter",
            "existing_pavement": "Existing pavement",

        }


class InfrastructureProjectCreateForm(InfrastructureProjectBaseForm):
    pass


class InfrastructureProjectEditForm(InfrastructureProjectBaseForm):
    pass


class InfrastructureProjectDeleteForm(InfrastructureProjectBaseForm):
    pass

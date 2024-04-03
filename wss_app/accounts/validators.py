from django.core import validators


def validate_picture_file_size(picture_object):
    if picture_object.size > 3145728:
        raise validators.ValidationError("The maximum picture file size should not exceed 3MB!")

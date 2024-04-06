from django import template
from django import forms

register = template.Library()


@register.filter
def placeholder(field, token):
    field.field.widget.attrs['placeholder'] = token
    return field


@register.filter(name='add_class')
def add_class(field, css_class):
    if hasattr(field, 'field'):
        widget = field.field.widget
        if isinstance(widget, (forms.Select, forms.SelectMultiple)):
            widget.attrs['class'] = f'{widget.attrs.get("class", "")} form-select {css_class}'
        else:
            widget.attrs['class'] = f'{widget.attrs.get("class", "")} {css_class}'
        return field
    else:
        return field


@register.filter
def get_range(value):
    return range(value)


@register.filter
def get_empty_range(value):
    return range(5 - value)

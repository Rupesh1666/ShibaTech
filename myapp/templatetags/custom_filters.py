from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg

@register.filter
def to_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return 0

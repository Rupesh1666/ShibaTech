# myapp/templatetags/cart_filters.py
from django import template

register = template.Library()

@register.filter
def total_amount(cart):
    return sum(item['total_price'] for item in cart)



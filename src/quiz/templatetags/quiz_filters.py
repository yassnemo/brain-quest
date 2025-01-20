from django import template

register = template.Library()

@register.filter
def percentage(value, total):
    try:
        return int((value / total) * 100)
    except (ValueError, ZeroDivisionError):
        return 0
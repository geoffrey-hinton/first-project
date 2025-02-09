from django import template

register = template.Library()

@register.filter
def concat(value, args):
    return f"{value}{args}"


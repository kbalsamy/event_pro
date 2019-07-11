from django import template
from django.utils.html import format_html


register = template.Library()


@register.filter(name='svg')
def get_layout_svg(value):

    return format_html(value.decode())

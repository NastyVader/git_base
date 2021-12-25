from django import template

register = template.Library()

@register.simple_tag(name='trial')
def trial(value):

    return '1'

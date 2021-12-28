from django import template

register = template.Library()

i=1
@register.simple_tag
def trial():
    if i==1:return i




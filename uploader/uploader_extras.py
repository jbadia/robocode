from django import template

register = template.Library()

@register.filter
def IN(value,arg): 
    return value in arg 

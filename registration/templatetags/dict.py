from django import template

register = template.Library()

@register.filter
def getValue(cdictionary, key):
    print(cdictionary)
    return cdictionary[key]
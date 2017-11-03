from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    return value.replace(arg, '')

def add(value,arg):
    return value.add(arg, '')

def asdf(value,arg):
    return value.add(arg, '')

#register.filter('cut', cut)
register.filter('add', add)
register.filter('asdf', asdf)

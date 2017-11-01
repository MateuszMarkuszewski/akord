from django import template

register = template.Library()


@register.filter
def make_ref_to_id(value):
    return "#{0}".format(value)

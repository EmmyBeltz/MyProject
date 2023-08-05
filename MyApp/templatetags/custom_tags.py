from django import template
register = template.Library()

@register.simple_tag
def get_obj(queryset, pk, attr):
    obj = getattr(queryset.get(pk=int(pk)), attr)
    return obj

@register.simple_tag
def split_by_symbol(input_string, symbol):
    return input_string.split(symbol)
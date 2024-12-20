from django import template

register = template.Library()

@register.filter(name="lower_words")
def lower_words(value,max_lenght=100):
    if len(value) > max_lenght:
        return value[:max_lenght] + "..."
    return value

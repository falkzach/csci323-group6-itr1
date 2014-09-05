from django import template
import re


register = template.Library()
@register.tags
def active(request, pattern):

    if re.search(pattern, request.path):
        return 'active'
    return ''
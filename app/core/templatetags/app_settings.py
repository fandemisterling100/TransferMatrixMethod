from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag(name="app_settings")
def app_settings_tag():
    return settings

from django.conf import settings
from django.core.cache import cache, caches


def app_cache():
    return caches["admin_interface"] if "admin_interface" in settings.CACHES else cache


def del_cached_active_theme(_site=None):
    app_cache().delete(f"admin_interface_theme_{_site}")

def get_cached_active_theme(_site=None):
    return app_cache().get(f"admin_interface_theme_{_site}", None)

def set_cached_active_theme(theme, _site=None):
    app_cache().set(f"admin_interface_theme_{_site}", theme)

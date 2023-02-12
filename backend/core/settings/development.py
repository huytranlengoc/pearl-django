from .base import *  # noqa

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_COLLAPSED": True,
}

INSTALLED_APPS += ["debug_toolbar"]

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

INTERNAL_IPS = ["127.0.0.1"]

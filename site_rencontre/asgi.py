"""
ASGI config for site_rencontre project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.sessions import SessionMiddlewareStack
import app_messages.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'site_rencontre.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": SessionMiddlewareStack(
        URLRouter(
            app_messages.routing.websocket_urlpatterns
        )
    ),
})

"""
ASGI config for channels_temp0 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channels_temp0.settings')

django_asgi_app = get_asgi_application()

import chat.routing

# From the scope of the outside channels_temp0 folder, in terminal: hypercorn myproject.asgi:application
# Using a specific address: hypercorn myproject.asgi:application --bind '192.168.150.129:8000'

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(URLRouter(chat.routing.websocket_urlpatterns))
    ),
})
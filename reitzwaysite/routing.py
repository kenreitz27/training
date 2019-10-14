from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
#from posting.consumers import ws_connect, ws_disconnect

from posting.consumers import MessageConsumer


application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
  'websocket': AllowedHostsOriginValidator(
    AuthMiddlewareStack(
      URLRouter(
        [
          path("posting/monitor-<int:event_pk>/", MessageConsumer),
        ]
      )
    )
  )
})

# channel_routing = [
# #   route('websocket.connect', ws_connect),
# #   route('websocket.disconnect', ws_disconnect),
# ]

#          url(r"^posting/monitor-<int:event_pk>/", MessageConsumer),

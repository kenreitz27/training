from channels.routing import ProtocolTypeRouter
#from posting.consumers import ws_connect, ws_disconnect

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
})

# channel_routing = [
# #   route('websocket.connect', ws_connect),
# #   route('websocket.disconnect', ws_disconnect),
# ]
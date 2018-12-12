from channels.routing import route
from xws.consumers import ws_connect, ws_receive, ws_disconnect

channel_routing = [
    route('websocket.connect', ws_connect),
    route("websocket.receive", ws_receive),
    route('websocket.disconnect', ws_disconnect),
]

# channel_routing = [
#     route("websocket.connect", ws_connect, path=r"^/(?P<room_name>[a-zA-Z0-9_]+)/$"),
#     route("websocket.receive", ws_receive, path=r"^/(?P<room_name>[a-zA-Z0-9_]+)/$"),
#     route("websocket.disconnect", ws_disconnect, path=r"^/(?P<room_name>[a-zA-Z0-9_]+)/$"),
# ]
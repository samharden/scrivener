from . import transcribe

channel_routing = {

    'websocket.connect': transcribe.ws_connect,
    'websocket.receive': transcribe.ws_receive,
    'websocket.disconnect': transcribe.ws_disconnect,

}

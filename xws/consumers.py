import json
from channels import Group, Channel
from channels.auth import channel_session_user, channel_session_user_from_http

rooms = {
    'general': {
        'title': 'this is general chat',
        'users_online': []
    },
    'second_chat': {
        'title': 'this is another general chat',
        'users_online': []
    },
    'lobby': {
        'title' :'lobby',
        'users_online': []
    }
}

clients = dict()


def create_message(type, payload):
    return {
        'text': json.dumps({
            'type': type,
            'payload': payload,
        })
    }


def send_users_online(room):
    global rooms

    msg = create_message('users_online', rooms[room]['users_online'])
    send_to_room(room, msg)


def send_to_room(room, message):
    global rooms, clients

    for name in clients:
        if clients[name] == room:
            Channel(name).send(message)


def send_rooms(channel):
    global rooms
    payload = [{'title': rooms[room]['title'], 'name': room} for room in rooms]
    channel.send(create_message('rooms', payload))


def get_user_from_message(message):
    return {
        'id': message.user.id,
        'username': message.user.username,
    }


def enter_room(message, room_name):
    global rooms, clients

    user = get_user_from_message(message)

    if user not in rooms[room_name]['users_online']:
        rooms[room_name]['users_online'].append(user)

    print("add connection to group %s" % room_name)


    clients[message.reply_channel.name] = room_name
    send_users_online(room_name)


def leave_room(message, room_name):
    global rooms

    # Group(room_name).discard(message.reply_channel)

    user = get_user_from_message(message)

    if user in rooms[room_name]['users_online']:
        rooms[room_name]['users_online'].remove(user)

    clients[message.reply_channel.name] = None
    send_users_online(room_name)



@channel_session_user_from_http
def ws_connect(message):
    global clients
    room_name = 'general'

    print("ws_connect %s to room: %s" % (message.reply_channel.name, room_name))

    clients[message.reply_channel.name] = room_name

    message.reply_channel.send({"accept": True})
    enter_room(message, room_name)
    send_rooms(message.reply_channel)


@channel_session_user
def ws_receive(message):
    global clients

    room_name = clients[message.reply_channel.name]

    decoded_message = json.loads(message["text"])

    username = message.user.username
    type, payload = decoded_message['type'], decoded_message['payload']

    print("ws_receive room: %s type: %s payload: %s" % (room_name, type, payload))

    if type == 'message':
        payload = {
                'username': username,
                'text': payload
        }
        send_to_room(room_name, create_message('new_message', payload))
    elif type == 'change_room':
        new_room = payload
        print("user goes from %s to %s" % (room_name, new_room))
        leave_room(message, room_name)
        enter_room(message, new_room)
        message.reply_channel.send(create_message('change_room', new_room))
    else:
        print("unknown type: %s" % type)


@channel_session_user
def ws_disconnect(message):
    room_name = clients[message.reply_channel.name]
    print("ws_disconnect room: %s" % room_name)
    leave_room(message, room_name)

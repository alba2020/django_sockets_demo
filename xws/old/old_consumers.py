import json
from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http

from django.contrib.auth import get_user_model

rooms = {
    'general': {
        'title': 'this is general chat',
        'users_online': []
    },
    'second_chat': {
        'title': 'this is another general chat',
        'users_online': []
    }
}

def send_users_online(room):
    global rooms

    print("send users for room %s" % room)

    Group(room).send({
        'text': json.dumps({
            'type': 'users_online',
            'payload': rooms[room]['users_online'],
        })
    })


@channel_session_user_from_http
def ws_connect(message, room_name):
    print("ws_connect room: %s" % room_name)

    global rooms
    message.reply_channel.send({"accept": True})

    user = {
        'id': message.user.id,
        'username': message.user.username,
    }

    if user not in rooms[room_name]['users_online']:
        rooms[room_name]['users_online'].append(user)

    print("add connection to group %s" % room_name)
    Group(room_name).add(message.reply_channel)

    send_users_online(room_name)

    # users = User.objects.select_related('logged_in_user')
    # for user in users:
    #      user.status = 'Online' if hasattr(user, 'logged_in_user') else 'Offline'


    # Group('users').send({
    #     'text': json.dumps({
    #         'type': 'users_online',
    #         'payload': [
    #                         {
    #                             'id': '0',
    #                             'username':'John',
    #                         },
    #                         {
    #                             'id': '1',
    #                             'username': 'Paul',
    #                         },
    #                         {
    #                             'id': '2',
    #                             'username': 'Kiska'
    #                         }
    #                     ],
    #     })
    # })

@channel_session_user
def ws_receive(message, room_name):
    decoded_message = json.loads(message["text"])

    username = message.user.username
    type, payload = decoded_message['type'], decoded_message['payload']

    print("ws_receive room: %s type: %s payload: %s" % (room_name, type, payload))

    if type == 'message':
        Group(room_name).send({
            'text': json.dumps({
                'type': 'new_message',
                'payload': {
                    'username': username,
                    'text': payload
                },
            })
        })
    else:
        print("unknown type")



@channel_session_user
def ws_disconnect(message, room_name):
    print("ws_disconnect room: %s" % room_name)
    global rooms

    # Group('users').send({
    #     'text': json.dumps({
    #         'username': message.user.username,
    #         'is_logged_in': False
    #     })
    # })
    Group(room_name).discard(message.reply_channel)

    user = {
        'id': message.user.id,
        'username': message.user.username,
    }

    if user in rooms[room_name]['users_online']:
        rooms[room_name]['users_online'].remove(user)

    send_users_online(room_name)

    # message.reply_channel.send({"accept": True})
    # print("ws connect")

    # User = get_user_model()
    
    # users_online = [{
    #                     'id': user.id,
    #                     'username': user.username
    #                 }
    #                 for user in User.objects.select_related('logged_in_user')
    #                 if hasattr(user, 'logged_in_user')]

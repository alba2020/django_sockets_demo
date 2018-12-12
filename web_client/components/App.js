import React, { Component } from 'react'
import PropTypes from 'prop-types'
import UserList from './UserList'
import MessageList from './MessageList'
import Input from './Input'
import Room from './Room'
import Lobby from './Lobby'

class App extends Component {

    state = {
        users_online: [
            {
                username: 'you are offline',
                id: 0
            }
        ],
        messages: [
            {
                username: 'John',
                text: 'Hello'
            },
            {
                username: 'Jim',
                text: 'I love you'
            }
        ],
        rooms: [
            {
                title: 'general chat for everybody',
                name: 'general'
            },
            {
                title: 'another chat',
                name: 'chat2'
            }
        ],
        current_room: 'general'
    }

    constructor(props) {
        super(props)

        // localStorage.getItem("ws_url") ||

        const ws_url =  'ws://' + window.location.host + '/general/'
        console.log("connecting to", ws_url)
        this.socket = new WebSocket(ws_url)

        this.socket.onopen = function open() {
            console.log('WebSockets connection created.')
        }

        this.socket.onmessage = function message(event) {
            // console.log('--socket.onmessage--')
            const {type, payload} = JSON.parse(event.data)

            console.log(type, ':', payload)

            switch(type) {
                case 'rooms':
                    this.setState({ rooms: payload })
                    break
                case 'users_online':
                    this.setState({ users_online: payload })
                    break
                case 'new_message':
                    this.setState({ messages: [...this.state.messages, payload] })
                    break
                case 'change_room':
                    this.setState({ current_room: payload, messages: [] })
                    break
            }
        }.bind(this);

        if (this.socket.readyState == WebSocket.OPEN) {
            this.socket.onopen();
        }

        this.socket.onclose = function() {
            console.log('closing ws connection');
        }
    }

    sendMessage = (msg) => {
        console.log('sending message', msg)
        const to_send = {
            type: 'message',
            payload: msg
        }
        this.socket.send(JSON.stringify(to_send))
    }

    renderRoom() {
        const { users_online, messages, current_room } = this.state

        return (
            <div>
                <Room
                    users_online={ users_online }
                    messages={ messages }
                    sendMessage={ this.sendMessage }
                    changeRoom={ this.changeRoom }
                    roomName={ current_room }
                />
            </div>
        )
    }

    changeRoom = (roomName) => {
        return (e) => {
            e.preventDefault()
            console.log('go to', roomName)
            // this.setState({
            //     current_room: roomName
            // })
            const to_send = {
                type: 'change_room',
                payload: roomName
            }
            this.socket.send(JSON.stringify(to_send))
        }
    }

    renderLobby() {
        return (
            <div>
                <Lobby rooms={ this.state.rooms } changeRoom={ this.changeRoom } />
            </div>
        )
    }

    render() {
        if (this.state.current_room && this.state.current_room !== 'lobby')
            return this.renderRoom();
        else
            return this.renderLobby();

        // return (
        //     <div>
        //         <h1 className="chat_header">Chat</h1>
        //         <div className="col-md-8 col-sm-8 col-xs-8">
        //             <MessageList messages={ messages }/>
        //             <Input sendMessage={ this.sendMessage }/>
        //         </div>
        //         <div className="col-md-4 col-sm-4 col-xs-4">
        //             <UserList users={ users_online }/>
        //         </div>
        //     </div>
        // )
    }
}

export default App
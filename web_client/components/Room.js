import React, { Component } from 'react'
import PropTypes from 'prop-types'
import UserList from './UserList'
import MessageList from './MessageList'
import Input from './Input'

class Room extends Component {

    static propTypes = {
        users_online: PropTypes.arrayOf(PropTypes.shape({
            id: PropTypes.number.isRequired,
            username: PropTypes.string.isRequired,
        })).isRequired,

        messages: PropTypes.arrayOf(PropTypes.shape({
            username: PropTypes.string.isRequired,
            text: PropTypes.string.isRequired
        })).isRequired,

        sendMessage: PropTypes.func.isRequired
    }


    render() {
        const { users_online, messages, sendMessage, changeRoom, roomName } = this.props

        return (
            <div>
                <h2 className="room_header">Room { roomName }</h2>
                <a href="lobby" onClick={ changeRoom('lobby') }>to lobby</a>
                <div className="col-md-8 col-sm-8 col-xs-8">
                    <MessageList messages={ messages }/>
                    <Input sendMessage={ sendMessage }/>
                </div>
                <div className="col-md-4 col-sm-4 col-xs-4">
                    <UserList users={ users_online }/>
                </div>
            </div>
        )
    }
}

export default Room
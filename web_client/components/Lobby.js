import React, { Component } from 'react'
import PropTypes from 'prop-types'

class Lobby extends Component {

    static propTypes = {
        rooms: PropTypes.arrayOf(PropTypes.shape({
            title: PropTypes.string.isRequired,
            name: PropTypes.string.isRequired,
        })).isRequired,
        changeRoom: PropTypes.func.isRequired
    }


    render() {
        const { rooms, changeRoom } = this.props

        return (
            <div className="room_list">
                <h3>rooms</h3>
                <ul>
                    {
                        rooms.map((room, i) =>
                            <li key={ i }>
                                <a href={room.name} onClick={ changeRoom(room.name) }>{ room.title }</a>
                            </li>)
                    }
                </ul>
            </div>
        )
    }
}

export default Lobby
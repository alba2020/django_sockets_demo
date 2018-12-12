import React, { Component } from 'react'
import PropTypes from 'prop-types'
import './MessageList.css'

class MessageList extends Component {

    static propTypes = {
        messages: PropTypes.arrayOf(PropTypes.shape({
            username: PropTypes.string.isRequired,
            text: PropTypes.string.isRequired
        })).isRequired
    }

    render() {
        const { messages } = this.props
        
        return (
            <div className="message_list">
                <h3>messages</h3>
                <ul>
                    {
                        messages.map((msg, i) =>
                            <li key={ i }>{ msg.username }: { msg.text }</li>)
                    }
                </ul>
            </div>
         )
    }
}


export default MessageList

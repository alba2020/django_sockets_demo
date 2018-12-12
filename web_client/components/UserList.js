import React, { Component } from 'react'
import PropTypes from 'prop-types'
import User from './User'

class UserList extends Component {

    static propTypes = {
        users: PropTypes.arrayOf(PropTypes.shape({
            id: PropTypes.number.isRequired,
            username: PropTypes.string.isRequired,
        })).isRequired
    }

// an array of a particular shape.

    render() {
        const { users } = this.props
        
        return (
            <div className="user_list">
                <h3>users online</h3>
                <ul>
                    {
                        users.map(user =>
                            <User key={ user.id } user={ user }/> )
                    }
                </ul>
            </div>
         )
    }
}


export default UserList

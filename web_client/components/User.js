import React, { Component } from 'react'
import PropTypes from 'prop-types'

class User extends Component {

    static propTypes = {
        user: PropTypes.shape({
            id: PropTypes.number.isRequired,
            username: PropTypes.string.isRequired,
        }).isRequired
    }


    render() {
        const { username } = this.props.user
        return (
            <li>{ username } </li>
        )
    }
}


export default User

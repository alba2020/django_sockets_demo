import React, { Component } from 'react'
import PropTypes from 'prop-types'

class Input extends Component {

    static propTypes = {
        sendMessage: PropTypes.func.isRequired
    }

    state = {
        message: ''
    }

    handleChange = e => {
        this.setState({ message: e.target.value })
    }

    handleSubmit = e => {
        e.preventDefault()
        // console.log('message: ' + this.state.message)
        this.props.sendMessage(this.state.message)
        this.setState({ message: '' })
    }

    render() {
        return (
            <div className="input_message">
                <form onSubmit={this.handleSubmit}>
                <label>
                    Message:
                    <input type="text" id="input_message" value={this.state.message}
                        onChange={this.handleChange} />
                </label>
                <input type="submit" id="input_submit" value="Submit" />
                </form>
            </div>
          )
    }
}

export default Input
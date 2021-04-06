import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { addLeads } from '../../actions/leads';


class Form extends Component {
    state = {
        name: '',
        email: '',
        message: ''
    }

    static propTypes = {
        addLeads: PropTypes.func.isRequired
    }

    onChange = e => this.setState({ [e.target.name]: e.target.value });
    onSubmit = e => {
        e.preventDefault()
        const { name, email, message } = this.state;
        const lead = { name, email, message };
        this.props.addLeads(lead);
        this.setState = ''
    }

    render() {
        const { name, email, message } = this.state;
        return (
            <React.Fragment>
                <form onSubmit={this.onSubmit}>
                    <div className="form-group">
                        <label>Name *</label>
                        <input type="text" className="form-control" name="name" value={name} onChange={this.onChange} placeholder="Enter Your Name" />
                    </div>
                    <div className="form-group">
                        <label>Email address *</label>
                        <input type="email" className="form-control" name="email" onChange={this.onChange} value={email} placeholder="name@example.com" />
                    </div>
                    <div className="form-group">
                        <label>Message</label>
                        <textarea name="message" className="form-control" onChange={this.onChange} value={message}></textarea>
                    </div>
                    <div className="form-group">
                        <input type="submit" name="submit" className="btn btn-success" />
                    </div>
                </form>
            </React.Fragment>
        )
    }
}


export default connect(null, { addLeads })(Form)

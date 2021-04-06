import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { getLeads, deleteLeads } from '../../actions/leads';
import leads from '../../reducers/leads';

export class Lead extends Component {
    static propTypes = {
        leads: PropTypes.array.isRequired,
        getLeads: PropTypes.func.isRequired,
        deleteLeads: PropTypes.func.isRequired,
    }

    componentDidMount() {
        this.props.getLeads();
    }

    render() {
        return (
            <>
                <h2>Leads List</h2>
                <table className="table table-striped">
                    <thead>
                        <tr>
                            <th>Id</th>
                            <th>Name</th>
                            <th>Email</th>
                            <th>Message</th>
                            <th />
                        </tr>
                    </thead>
                    <tbody>
                        {this.props.leads.map((lead, index) => (
                            <tr key={lead.id}>
                                <td>{index + 1}</td>
                                <td>{lead.name}</td>
                                <td>{lead.email}</td>
                                <td>{lead.message}</td>
                                <td><button onClick={this.props.deleteLeads.bind(this, lead.id)} className="btn btn-danger btn-sm">Delete</button></td>

                            </tr>
                        ))}
                    </tbody>
                </table>
            </>
        )
    }
}

const mapStateToProps = state => ({
    leads: state.leads.leads
});

export default connect(mapStateToProps, { getLeads, deleteLeads })(Lead)

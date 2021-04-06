import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import Header from './layouts/Header';
import Dashboard from './leads/Dashboard';
import Alerts from './layouts/Alerts';

import { Provider } from 'react-redux';
import { Provider as AlertProvider } from 'react-alert';
import AlertTemplate from 'react-alert-template-basic'

import store from '../store'

// alert Options
const alertOptions = {
    timeout: 3000,
    position: 'top center',
}
class App extends Component {
    render() {
        return (
            <Provider store={store}>
                <AlertProvider template={AlertTemplate} {...alertOptions}>
                    <Header />
                    <Alerts />
                    <div className="container">
                        <Dashboard />
                    </div>
                </AlertProvider>
            </Provider>
        )
    }
}

ReactDOM.render(<App />, document.getElementById('app'));
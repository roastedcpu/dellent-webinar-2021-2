import React, { Component } from 'react';
import { render } from 'react-dom';
import UserList from './UserList';
import './style.css';

class App extends Component {
  constructor() {
    super();
    this.state = {
      name: 'React'
    };
  }

  render() {
    return (
      <div id = "bg">
        <UserList />
      </div>
    );
  }
}

render(<App />, document.getElementById('root'));

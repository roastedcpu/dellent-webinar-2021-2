import React, { Component } from 'react';

import './style.css';

class UserList extends Component {
  constructor() {
    super();
    this.state = {
      items: [],
    };
  }

  componentDidMount() {
    fetch(process.env.REACT_APP_API_URL)
      .then((results) => {
        return results.json();
      })
      .then((data) => {
        console.log(data)
        let users = data.results.map((user) => {
          return (
            <tr key={user.login.uuid}>
              <td>{user.login.username}</td>
              <td>
                {user.name.first} {user.name.last}
              </td>
            </tr>
          );
        });
        this.setState({
          items: users,
        });
      });
  }

  render() {
    return (
      <div>
        <table>
          <thead>
            <tr>
              <th>username</th>
              <th>name</th>
            </tr>
          </thead>
          <tbody>{this.state.items}</tbody>
        </table>
      </div>
    );
  }
}

export default UserList;

import logo from './logo.svg';
import './App.css';
import React from 'react';
import { render } from 'react-dom';
import HomePage from './views/homepage';
import {
  BrowserRouter as Router,
  Switch,
  Route
} from "react-router-dom";
export default class App extends React.PureComponent {
  render () {
    return (
      <Router>
        <Switch>
            <Route path="/">
              <HomePage/>
            </Route>
        </Switch>
      </Router>
    )    
  }
}



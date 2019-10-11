import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

class GreetingForm extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      name: '',
      funFact: '',
    }

    this.handleNameChange = this.handleNameChange.bind(this)
    this.handleFunFactChange = this.handleFunFactChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  handleNameChange(event) {
    this.setState({name: event.target.value});
  }

  handleFunFactChange(event) {
    this.setState({funFact: event.target.value});
  }

  handleSubmit(event) {
    alert('Hi ' + this.state.name + '. Your fun fact is ' + this.state.funFact);
    this.setState({
      name: '',
      funFact: '',
    });
    event.preventDefault();
  }

  render() {
    return(
      <form onSubmit={this.handleSubmit}>
        <lable>
          Name:
          <input type="text" value={this.state.name} onChange={this.handleNameChange} />
        </lable>
        <lable>
          Fun Fact:
          <input type="text" value={this.state.funFact} onChange={this.handleFunFactChange} />
        </lable>
        <input type="submit" value="Submit"/>
      </form>
    )
  }
}

// ========================================

ReactDOM.render(
  <GreetingForm />,
  document.getElementById('root'),
);

document.title = "Team Introduction"
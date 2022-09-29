import React, { PureComponent } from 'react';
import { View, Text, Button, Alert } from 'react-native';

import Step from './Step';

class Wizard extends PureComponent {
  static Step = Step;

  state = {
    index: 0,

    values: {
      ...this.props.initialValues,
    },
  };

  _nextStep = () => {
    if (this.state.index !== this.props.children.length - 1) {
      this.setState(prevState => ({
        index: prevState.index + 1,
      }));
    }
  };

  _prevStep = () => {
    if (this.state.index !== 0) {
      this.setState(prevState => ({
        index: prevState.index - 1,
      }));
    }
  };

  _onChangeValue = (name, value) => {
    this.setState(prevState => ({
      values: {
        ...prevState.values,
        [name]: value,
      },
    }));
  };

  _onSubmit = () => {
    Alert.alert(JSON.stringify(this.state.values));
  };

  render() {
    console.log('values', this.state);
    return (
      <View style={{ flex: 1 }}>
        {React.Children.map(this.props.children, (el, index) => {
          if (index === this.state.index) {
            return React.cloneElement(el, {
              currentIndex: this.state.index,
              nextStep: this._nextStep,
              prevStep: this._prevStep,

              isLast: this.state.index === this.props.children.length - 1,
              
              onChangeValue: this._onChangeValue,
              values: this.state.values,
              onSubmit: this._onSubmit,
            });
          }

          return null;
        })}
      </View>
    );
  }
}

export default Wizard;
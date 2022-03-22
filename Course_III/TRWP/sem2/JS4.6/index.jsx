class Hello extends React.Component {

  constructor(props) {
    super(props);
    this.state = {class: "off", label: "Нажмите"};
      
    this.press = this.press.bind(this);
  }

  press(){
    let className = (this.state.class==="off") ? "on":"off";
    this.setState({class: className});
  }
  render() {
    
    return  <div>
    <p>Имя: {this.props.name}</p>
    <p>Возраст: {this.props.age}</p>
    <button onClick={this.press} className={this.state.class}>{this.state.label}</button></div>;
  }
}

ReactDOM.render(
  <Hello name="Деменчук Георгий" age="22" />,
  document.getElementById("app")
)


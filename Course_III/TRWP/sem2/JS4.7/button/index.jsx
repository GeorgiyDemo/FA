class ClickButton extends React.Component {

  constructor(props) {
      super(props);
      this.state = {class: "off", label: "Нажми"};
         
      this.press = this.press.bind(this);
         
      console.log("constructor");
  }
  static getDerivedStateFromProps(props, state) {
       console.log("getDerivedStateFromProps()");
       return null;
  }
  componentDidMount(){
      console.log("componentDidMount()");
  }
  componentWillUnmount(){
      console.log("componentWillUnmount()");
  }
  shouldComponentUpdate(){
      console.log("shouldComponentUpdate()");
      return true;
  }
  getSnapshotBeforeUpdate(prevProps, prevState) {
     console.log("getSnapshotBeforeUpdate()");
     return null;
 }
  componentDidUpdate(){
      console.log("componentDidUpdate()");
  }
  press(){
      var className = (this.state.class==="off")?"on":"off";
      this.setState({class: className});
  }
  render() {
      console.log("render()");
      return <button onClick={this.press} className={this.state.class}>{this.state.label}</button>;
  }
}
ReactDOM.render(
  <ClickButton />,
  document.getElementById("app")
)
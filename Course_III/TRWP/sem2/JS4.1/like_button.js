'use strict';

const e = React.createElement;

class LikeButton extends React.Component{
    constructor(props) {
        super(props);
        this.state = {liked: false};
    }

    render() {
        if (this.state.liked){
            return "Раз раз";
        }

        return e(
            "button",
            {onClick: () => this.setState({liked: true})},
            "Like"
        );
    }
}


ReactDOM.render(e(LikeButton), document.querySelector("#like_button_container"));
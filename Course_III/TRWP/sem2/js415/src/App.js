import React from "react"






function App (props){

    return (
        <div className="Comment">
            <div className="UserInfo">
                <img className="Avatar"
                     src={this.props.author.avatarUrl}
                     alt={this.props.author.name}
                />
                <div className="UserInfo-name">
                    {this.props.author.name}
                </div>
            </div>
            <div className="Comment-text">
                {this.props.text}
            </div>
            <div className="Comment-date">
                {props.date}
            </div>
        </div>
    );
}

export default App
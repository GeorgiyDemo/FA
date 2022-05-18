import React, {Component} from 'react';
import TaskItem from './TaskItem';

export default class TaskList extends Component {
    render() {
        return (
            <table>
                <thead>
                <tr>
                    <th>Задание</th>
                    <th>Действия</th>
                </tr>
                </thead>
                <tbody>
                {this.props.tasks.map((task, index) => (
                    <TaskItem
                        key={index}
                        taskItem={task}
                        id={index}
                        deleteTask={this.props.deleteTask}
                        editTask={this.props.editTask}
                        toggleTask={this.props.toggleTask}
                    />
                ))}
                </tbody>
            </table>
        );
    }
}

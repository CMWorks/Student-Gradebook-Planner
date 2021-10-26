import React, { Component } from "react";

class Assignment extends Component {
  render() {
    const { assignmentName, pointsReceived, pointsTotal, percentGrade } =
      this.props;
    return (
      <div>
        <li className="list-group-item">
          Assignment Name Points Received Total Points Percent Grade
        </li>
        <li className="list-group-item">
          {assignmentName} {pointsReceived} {pointsTotal} {percentGrade}
        </li>
      </div>
    );
  }
}

export default Assignment;

import React from "react";
import ToDoListItem from "./ToDoListItem";

class Home extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      unfinishedAssignments: [], 
      checked: {},
      isNoneClicked: false,
    };
    this.getAssignmentsFromTable();
  }

  getAssignmentsFromTable = async () => {
    this.props.server.getAllFromTable('assignments', 'userID', this.props.userData.userID).then(retrieve => {
      let assignments = retrieve.data;
      let localUnfinishedAssignments = [];

      // Create a local array of unfinished assignments.
      for (let i = 0; i < assignments.length; i++) {
        if (!assignments[i].isDone) {
          localUnfinishedAssignments.push(assignments[i]);
        }
      }
      // Create a local object to track the condition of each assignment.
      let localChecked = localUnfinishedAssignments.reduce(
        (asgIDs, asg) => ({
          ...asgIDs,
          [asg.assignmentID]: false,
        }),
        {}
      );
      // Assign the state the values of the local array and object.
      this.setState({ unfinishedAssignments: localUnfinishedAssignments });
      this.setState({ checked: localChecked });
    });
  }

  handleCheckboxChange = (event) => {
    console.log("Check box got clicked!");
    console.log(event.target);

    // Capture the name (i.e., assignmentID) of the checkbox.
    const { name } = event.target;
    
    // Toggle the "checked" condition of the assignment that was just clicked.
    this.setState( (prevState) => ({
      checked: {
        ...prevState.checked,
        [name]: !prevState.checked[name]
      }
    }));

    // console.log(this.state.checked);
    
    // Check whether there are no check boxes clicked.
    // this.setState({ isNoneClicked: this.checkNoneClicked() });  // This method call does not quite work.
  }

  checkNoneClicked = () => {
    // Loop through the values of each assignment in state.
    for (let i = 0; i < this.state.unfinishedAssignments.length; i++) {
      // If one is checked, return false.
      let curAsg = this.state.unfinishedAssignments[i];
      if (this.state.checked[curAsg.assignmentID]) {
        console.log(" - Asg #"+curAsg.assignmentID+" is checked.");
        return false;
      }
    }
    // Otherwise, if program looped through all values, return true.
    console.log(" - No assignments checked.")
    return true;
  }

  handleSubmit = (event) => {
    event.preventDefault();
    console.log("Submit button got clicked!");
    console.log(event.target);
    console.log(this.state.checked);

    // Create two local arrays representing the still-unfinished and newly-finished assignments.
    let localUnfinishedAssignments = [];
    let finishedAssignments = []
    for (let i = 0; i < this.state.unfinishedAssignments.length; i++) {
      let curAsg = this.state.unfinishedAssignments[i];
      if (!this.state.checked[curAsg.assignmentID]) {
        // This assignment is still unfinished.
        localUnfinishedAssignments.push(curAsg);
      } else {
        // This is a newly-finised assignment.
        curAsg.isDone = true;
        finishedAssignments.push(curAsg);
      }
    }
    // Create a new checked object to track the still-unfinished assignments.
    let newChecked = localUnfinishedAssignments.reduce(
      (asgIDs, asg) => ({
        ...asgIDs,
        [asg.assignmentID]: false,
      }),
      {}
    );

    // Set the state to represent the new checked object and the still-unfinished assignments.
    this.setState({ unfinishedAssignments: localUnfinishedAssignments })
    this.setState({ checked: newChecked })

    // Update the server with the newly-finished assignments.
    for (let i = 0; i < finishedAssignments.length; i++) {
      let curAsg = finishedAssignments[i];
      this.props.server.updateUserData('assignments', curAsg.assignmentID, curAsg);
    }
  }

  createListItem = (assignment) => (
    <ToDoListItem 
      item={assignment}
      isSelected={this.state.checked[assignment.assignmentID]}
      onCheckboxChange={this.handleCheckboxChange}
      key={assignment.assignmentID}
    />
  );

  displayUnfinishedAssignments() {
    let array = [];

    // Insert all unfinished assignments into the list.
    for (let i = 0; i < this.state.unfinishedAssignments.length; i++) {
      array.push(
        this.createListItem(this.state.unfinishedAssignments[i])
      );
    }
    // console.log(this.state.checked);
    // console.log(array);
    return array;
  }

  render() {
    // this.getAssignmentsFromTable();
    return (
      <div className="home">
        <div className="container">
          <div className="row align-items-center my-5">
            <div className="col-lg-7">
              <img
                className="img-fluid rounded mb-4 mb-lg-0"
                src="http://placehold.it/900x400"
                alt=""
              />
            </div>
            <div className="col-lg-5">
              <h1 className="font-weight-light">Home</h1>
              <p>
                Lorem Ipsum is simply dummy text of the printing and typesetting
                industry. Lorem Ipsum has been the industry's standard dummy text
                ever since the 1500s, when an unknown printer took a galley of
                type and scrambled it to make a type specimen book.
              </p>
              <h2 className="font-weight-light">To-Do</h2>
              <form onSubmit={this.handleSubmit}>
                <ul>
                  { this.displayUnfinishedAssignments() }
                </ul>
                <button type="submit" className="btn btn-primary" disabled={this.state.isNoneClicked}>
                  Submit
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Home;
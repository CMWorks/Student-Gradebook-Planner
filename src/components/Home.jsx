import React from "react";

class Home extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      assignments: [],
      checkboxIDs: [],
      // checked: {},
    };
    this.getAssignmentsFromTable();
  }

  // componentDidMount = async () => {
  //   this.props.server.getAllFromTable('assignments', 'userID', this.props.userData.userID).then(retrieve => {
  //     console.log('success: ' + retrieve.success);
  //     this.setState({ assignments: retrieve.data });
  //   });
  // }

  getAssignmentsFromTable = async () => {
    this.props.server.getAllFromTable('assignments', 'userID', this.props.userData.userID).then(retrieve => {
      this.setState({ assignments: retrieve.data });
    });
  }

  handleCheckboxChange = (event) => {
    console.log("Check box got clicked!");
    console.log(event.target);
    // console.log(this.state.checked);
    // let asgID = +event.target.name;

    // // Get the index of the assignment that was just marked as complete.
    // let index = 0;
    // while (this.state.assignments[index].assignmentID != asgID) {
    //   index++;
    // }
    // console.log("index: " + index);
    // console.log(this.state.assignments[index]);

    // // Update the server, passing the updated assignment object into it.
    // let newAssignment = this.state.assignments[index];
    // newAssignment.isDone = true;
    // console.log(newAssignment);
    // this.props.server.updateUserData('assignments', asgID, newAssignment);
  }

  handleSubmit = (event) => {
    console.log("Submit button got clicked!");
    console.log(event.target);
    event.preventDefault();
  }

  displayUnfinishedAssignments() {
    let array = [];
    // console.log(this.state.assignments);

    // Insert all unfinished assignments into the list.
    for (let i = 0; i < this.state.assignments.length; i++) {
      if (this.state.assignments[i].isDone != true) {
        let asgID = this.state.assignments[i].assignmentID;
        array.push(
          <li key={asgID}>
            {/* Each list item displays the assignment name, due date, and a check box. */}
            {this.state.assignments[i].assignmentName} |  
            Due {this.state.assignments[i].dueDate} | 
            Done:
            <input
              type="checkbox"
              name={asgID}   // Each check box uses its corresponding assignment's ID to identify itself.
              onChange={this.handleCheckboxChange}
            /> 
          </li>
        );
        // this.setState( { checkboxIDs: checkboxIDs.append(asgID) } );
        
        // this.setState( (prevState) => {
        //   let checked = { ...prevState.checked };
        //   checked[asgID] = false;
        //   return { checked };
        // });
      }
    }
    console.log(this.state.checked);
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
                <button type="submit" className="btn btn-primary" disabled={false}>
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
import React from "react";

class Home extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      assignmentCategories: [],
      assignments: [],
    };
  }

  // componentDidMount = async () => {
  //   this.props.server.getAllFromTable('assignments', 'userID', this.props.userData.userID).then(retrieve => {
  //     console.log('success: ' + retrieve.success);
  //     this.setState({ assignments: retrieve.data });
  //   });
  // }

  getAssignmentsFromTable = async () => {
    this.props.server.getAllFromTable('assignments', 'userID', this.props.userData.userID).then(retrieve => {
      console.log('success: ' + retrieve.success);
      this.setState({ assignments: retrieve.data });
    });
  }


  displayUnfinishedAssignments() {
    let array = [];
    for (let i = 0; i < this.state.assignments.length; i++) {
      // If the assignment is unfinished, insert it into the list.
      if (this.state.assignments[i].isDone != true) {
        array.push(<li>{this.state.assignments[i].assignmentName}, due {this.state.assignments[i].dueDate}</li>);
      }
    }
    return array;
  }

  render() {
    this.getAssignmentsFromTable();
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
              <ul>
                { this.displayUnfinishedAssignments() }
              </ul>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Home;
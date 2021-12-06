import React from "react";
import Popup from "./Popup";
import { Link } from "react-router-dom";

class Semesters extends React.Component {
  constructor(props) {

    super(props);
    this.state = {
      semesters: [],
      courses: [],
      popUpButtonAddSemester: false,
      popUpButtonEditSemester: false,
      popUpButtonDeleteSemester: false,
      popUpButtonAddCourse: false,
      popUpButtonEditCourse: false,
      popUpButtonDeleteCourse: false,

      semesterName: '',
      semesterID: 0,
      gpa: 0.0,

      courseName: '',
      courseID: 0,
      creditHours: 0,
      courseType: '',
      grade: 0.0,
      isOnline: false,

      userID: this.props.userData.userID,
    };
    this.handleSubmitAddSemester = this.handleSubmitAddSemester.bind(this);
    this.handleSubmitDeleteSemester = this.handleSubmitDeleteSemester.bind(this);
    this.handleSubmitEditSemester = this.handleSubmitEditSemester.bind(this);
    this.handleChangeSemesterName = this.handleChangeSemesterName.bind(this);
    this.handleChangeSemesterID = this.handleChangeSemesterID.bind(this);

    this.handleSubmitAddCourse = this.handleSubmitAddCourse.bind(this);
    this.handleSubmitDeleteCourse = this.handleSubmitDeleteCourse.bind(this);
    this.handleChangeCourseName = this.handleChangeCourseName.bind(this);
    this.handleChangeCourseID = this.handleChangeCourseID.bind(this);
    this.handleSubmitEditCourse = this.handleSubmitEditCourse.bind(this);
    this.handleSubmitCourseName = this.handleSubmitCourseName.bind(this);
    this.handleSubmitCourseType = this.handleSubmitCourseType.bind(this)
    this.handleSubmitAddHours = this.handleSubmitAddHours.bind(this);
    this.handleChangeOnline = this.handleChangeOnline.bind(this);

  }



  componentDidMount = async () => {
    let id = this.props.userData.userID;
    this.props.server.getAllFromTable('semesters', 'userID', id).then(retrieve => {
      let success = retrieve.success;
      let data = retrieve.data;

      console.log('success: ' + success);
      this.setState({ semesters: retrieve.data });
      this.getCourseInfo();
    });
  }

  getCourseInfo = async () => {
    for (let i = 0; i < this.state.semesters.length; i++) {
      const response = await this.props.server.getAllFromTable('currentCourses', 'semesterID', this.state.semesters[i].semesterID).then(retrieve => {
        let success = retrieve.success;
        let data = retrieve.data;

        console.log('success: ' + success);
        return data;
      })
      this.setState({ courses: this.state.courses.concat(response) });
    }
  }

  displayCourses(semesterID) {
    let array = [];
    for (let m = 0; m < this.state.courses.length; m++) {
      // console.log(semesterID);
      // console.log(this.state.courses[m].semesterID);
      if (semesterID == this.state.courses[m].semesterID) {
        array.push(
          <ul key={this.state.courses[m].courseID}>
            <Link onClick={(event) => { this.props.set({ courseID: this.state.courses[m].courseID, courseName: this.state.courses[m].courseName, semesterID: this.state.courses[m].semesterID }) }}
              to={{
                pathname: this.props.baseLocation+"course",
              }}
            >{this.state.courses[m].courseName}</Link>
          </ul>
        );
      }
    }
    return array;
  }

  handleSubmitAddSemester(event) {
    //Create the semester object to send
    let Semester = {
      semesterID: this.props.server.generateID(),
      semesterName: this.state.semesterName,
      gpa: this.state.gpa,
      userID: this.props.userData.userID
    }
    console.log(Semester);
    if (this.state.semesterName === "") {
      event.preventDefault();
      document.getElementById("semesterName").classList.add("is-invalid")
      return
    }
    this.props.server.addUserData('semesters', Semester);
    this.setState({ popUpButtonAddSemester: false });
    event.preventDefault();
  }

  handleChangeSemesterName(event) {
    this.setState({ semesterName: event.target.value });
  }
  handleSubmitDeleteSemester(event) {
    if (this.state.semesterID === 0) {
      event.preventDefault();
      document.getElementById("deleteSemester").classList.add("is-invalid")
      return
    }
    if (this.state.semesterID === "0") {
      event.preventDefault();
      document.getElementById("deleteSemester").classList.add("is-invalid")
      return
    }
    this.props.server.deleteUserData('semesters', this.state.semesterID);
    this.setState({ popUpButtonDeleteSemester: false });
    event.preventDefault();

  }
  handleChangeSemesterID(event) {
    this.setState({ semesterID: event.target.value });
  }
  handleSubmitEditSemester(event) {
    let Semester = {
      semesterID: this.state.semesterID,
      semesterName: this.state.semesterName,
      gpa: 0,
      userID: this.props.userData.userID
    }
    if (this.state.semesterID === 0) {
      event.preventDefault();
      document.getElementById("semesterName").classList.add("is-invalid")
      return
    }
    if (this.state.semesterID === "") {
      event.preventDefault();
      document.getElementById("semesterName").classList.add("is-invalid")
      return
    }
    if (this.state.semesterName === "") {
      event.preventDefault();
      document.getElementById("semesterName1").classList.add("is-invalid")
      return
    }
    this.props.server.updateUserData('semesters', this.state.semesterID, Semester);
    this.setState({ popUpButtonEditSemester: false });
    event.preventDefault();

  }
  handleSubmitAddCourse(event) {
    let Course = {
      courseID: this.props.server.generateID(),
      courseName: this.state.courseName,
      creditHours: this.state.creditHours,
      courseType: this.state.courseType,
      userID: this.props.userData.userID,
      isOnline: this.state.isOnline,
      grade: this.state.grade,
      semesterID: this.state.semesterID
    }
    console.log(Course);
    if (this.state.semesterID === 0) {
      event.preventDefault();
      document.getElementById("semesterID").classList.add("is-invalid")
      return
    }
    if (this.state.semesterID === "") {
      event.preventDefault();
      document.getElementById("semesterID").classList.add("is-invalid")
      return
    }
    if (this.state.courseName === "") {
      event.preventDefault();
      document.getElementById("courseName").classList.add("is-invalid")
      return
    }

    if (this.state.creditHours > 16) {
      event.preventDefault();
      document.getElementById("creditHours").classList.add("is-invalid")
      return
    }
    this.props.server.addUserData('currentCourses', Course);
    this.setState({ popUpButtonAddCourse: false });
    event.preventDefault();
  }
  handleSubmitCourseName(event) {
    this.setState({ courseName: event.target.value });
  }
  handleChangeCourseName(event) {
    this.setState({ courseName: event.target.value });
  }
  handleChangeCourseID(event) {
    this.setState({ courseID: event.target.value });
  }
  handleChangeOnline(event) {
    this.setState({ isOnline: event.target.value });
  }
  handleSubmitDeleteCourse(event) {
    let Course = {
      courseID: this.props.server.generateID(),
      courseName: this.state.courseName,
      creditHours: this.state.creditHours,
      courseType: this.state.courseType,
      userID: this.props.userData.userID,
      isOnline: this.state.isOnline,
      grade: this.state.grade,
      semesterID: this.state.semesterID
    }
    console.log(Course);
    if (this.state.courseID === "") {
      event.preventDefault();
      document.getElementById("deleteCourse").classList.add("is-invalid")
      return
    }
    if (this.state.courseID === 0) {
      event.preventDefault();
      document.getElementById("deleteCourse").classList.add("is-invalid")
      return
    }

    this.props.server.deleteUserData('currentCourses', this.state.courseID);
    this.setState({ popUpButtonDeleteCourse: false });
    event.preventDefault();

  }
  handleSubmitEditCourse(event) {
    let Course = {
      courseID: this.state.courseID,
      courseName: this.state.courseName,
      creditHours: this.state.creditHours,
      courseType: this.state.courseType,
      userID: this.props.userData.userID,
      isOnline: this.state.isOnline,
      grade: this.state.grade,
      semesterID: this.state.semesterID
    }
    console.log(Course);
    if (this.state.semesterID === 0 || this.state.semesterID === "") {
      event.preventDefault();
      document.getElementById("semesterID").classList.add("is-invalid")
      return
    }
    if (this.state.courseID === 0 || this.state.semesterID === "") {
      event.preventDefault();
      document.getElementById("courseID").classList.add("is-invalid")
      return
    }


    console.log(Course);
    this.props.server.updateUserData('currentCourses', this.state.courseID, Course);
    this.setState({ popUpButtonEditCourse: false });
    event.preventDefault();
  }

  handleSubmitCourseType(event) {
    this.setState({ courseType: event.target.value });
  }
  handleSubmitAddHours(event) {
    this.setState({ creditHours: event.target.value })
  }

  render() {
    // console.log(this.state.semesters);
    // console.log(this.state.courses);
    return (
      <div className="semesters">
        <div className="container">
          <div className="row align-items-center my-5">
            <div className="col-lg-5" style={{ 'width': "100%" }}>
              <h1 className="font-weight-light">Semesters</h1>
              <button style={{ 'margin-left': "33px", 'marginBottom': "10px" }} className="btn btn-primary" onClick={() => this.setState({ popUpButtonAddSemester: true })}>
                Add Semester
              </button>
              <Popup trigger={this.state.popUpButtonAddSemester}>
                <h3>Add Semester</h3>
                <form className="form-floating" onSubmit={this.handleSubmitAddSemester}>
                  <div className="mb-3">
                    <label htmlFor="semesterName">Semester Name</label>
                    <input type="text" className="form-control" id="semesterName" onChange={this.handleChangeSemesterName} />

                  </div>

                </form>
                <button style={{ 'margin-right': "10px" }} className="btn btn-primary" onClick={this.handleSubmitAddSemester}>Submit</button>

                <button className="btn btn-primary" onClick={() => this.setState({ popUpButtonAddSemester: false })}>
                  Cancel
                </button>
              </Popup>
              <button style={{ 'margin-left': "33px", 'marginBottom': "10px" }} className="btn btn-primary" onClick={() => this.setState({ popUpButtonEditSemester: true })}>
                Edit Semester
              </button>
              <Popup trigger={this.state.popUpButtonEditSemester}>
                <h3>Edit Semester</h3>
                <form className="form-floating" onSubmit={this.handleSubmitEditSemester}>
                  <div className="mb-3">
                    <label htmlFor="semesterName">Old Semester Name</label>

                    <select className="form-control" id="semesterName" onChange={this.handleChangeSemesterID}>
                      <option value=''></option>
                      {this.state.semesters.map((semester) => (
                        <option value={semester.semesterID}>{semester.semesterName}</option>
                      ))}
                    </select>
                  </div>
                  <div className="mb-3">
                    <label htmlFor="categoryName">New Semester Name</label>
                    <input type="text" className="form-control" id="semesterName1" onChange={this.handleChangeSemesterName} />
                  </div>
                </form>
                <button style={{ 'margin-right': "10px" }} className="btn btn-primary" onClick={this.handleSubmitEditSemester}>Edit</button>
                <button className="btn btn-primary" onClick={() => this.setState({ popUpButtonEditSemester: false })}>
                  Cancel
                </button>
              </Popup>

              <button style={{ 'margin-left': "33px", 'marginBottom': "10px" }} className="btn btn-primary" onClick={() => this.setState({ popUpButtonDeleteSemester: true })}>
                Delete Semester
              </button>

              <Popup trigger={this.state.popUpButtonDeleteSemester}>
                <h3>Delete Semester</h3>

                <form className="form-floating" onSubmit={this.handleSubmitDeleteSemester}>
                  <div className="mb-3">
                    <label htmlFor="semester">Semester</label>
                    <select className="form-control" id="deleteSemester" onChange={this.handleChangeSemesterID}>\
                      <option value='0'></option>
                      {this.state.semesters.map((semester) => (
                        <option value={semester.semesterID}>{semester.semesterName}</option>
                      ))}
                    </select>
                  </div>
                </form>
                <button style={{ 'margin-right': "10px" }} className="btn btn-primary" onClick={this.handleSubmitDeleteSemester}>Delete</button>
                <button className="btn btn-primary" onClick={() => this.setState({ popUpButtonDeleteSemester: false })}>
                  Cancel
                </button>
              </Popup>

              <button style={{ 'margin-left': "33px", 'marginBottom': "10px" }} className="btn btn-primary" onClick={() => this.setState({ popUpButtonAddCourse: true })}>
                Add Course
              </button>
              <Popup trigger={this.state.popUpButtonAddCourse}>
                <h3>Add Course</h3>
                <form className="form-floating" onSubmit={this.handleSubmitAddCourse}>
                  <div className="mb-3">
                    <label htmlFor="semester">Semester</label>
                    <select className="form-control" id="semesterID" onChange={this.handleChangeSemesterID}>\
                      <option value=''></option>
                      {this.state.semesters.map((semester) => (
                        <option value={semester.semesterID}>{semester.semesterName}</option>
                      ))}
                    </select>
                  </div>
                  <div className="mb-3">
                    <label htmlFor="courseName">Course Name</label>
                    <input type="text" className="form-control" id="courseName" onChange={this.handleSubmitCourseName} />
                  </div>
                  <div className="mb-3">
                    <label htmlFor="courseType">Course Type</label>
                    <input type="text" className="form-control" id="courseType" onChange={this.handleSubmitCourseType} />
                  </div>
                  <div className="mb-3">
                    <label htmlFor="creditHours">Credit Hours</label>
                    <input type="number" className="form-control" id="creditHours" onChange={this.handleSubmitAddHours} />
                  </div>
                  <div className="mb-3">
                    <label htmlFor="isOnline">Online?</label>
                    <select className="form-control" id="online2" onChange={this.handleChangeOnline}>\
                      <option value=''></option>
                      <option value='true'>Yes</option>
                      <option value='false'>No</option>
                    </select>
                  </div>
                </form>
                <button style={{ 'margin-right': "10px" }} className="btn btn-primary" onClick={this.handleSubmitAddCourse}>Submit</button>

                <button className="btn btn-primary" onClick={() => this.setState({ popUpButtonAddCourse: false })}>
                  Cancel
                </button>
              </Popup>

              <button style={{ 'margin-left': "33px", 'marginBottom': "10px" }} className="btn btn-primary" onClick={() => this.setState({ popUpButtonEditCourse: true })}>
                Edit Course
              </button>
              <Popup trigger={this.state.popUpButtonEditCourse}>
                <h3>Edit Course</h3>
                <form className="form-floating" onSubmit={this.handleSubmitEditCourse}>
                  < div className="mb-3">
                    <label htmlFor="semester">Semester</label>
                    <select className="form-control" id="semesterID" onChange={this.handleChangeSemesterID}>\
                      <option value=''></option>
                      {this.state.semesters.map((semester) => (
                        <option value={semester.semesterID}>{semester.semesterName}</option>
                      ))}
                    </select>
                  </div>
                  <div className="mb-3">
                    <label htmlFor="courseName" id="courseName">Old Course Name</label>
                    <select className="form-control" id="courseID" onChange={this.handleChangeCourseID}>\
                      <option value=''></option>
                      {this.state.courses.map((course) => (
                        <option value={course.courseID}>{course.courseName}</option>
                      ))}
                    </select>
                  </div>
                  <div className="mb-3">
                    <label htmlFor="newCourseName">New Course Name</label>
                    <input type="text" className="form-control" id="courseName2" onChange={this.handleChangeCourseName} />
                  </div>
                  <div className="mb-3">
                    <label htmlFor="courseType">New Course Type</label>
                    <input type="text" className="form-control" id="courseType" onChange={this.handleSubmitCourseType} />
                  </div>
                  <div className="mb-3">
                    <label htmlFor="creditHours">New Credit Hours</label>
                    <input type="number" className="form-control" id="creditHours" onChange={this.handleSubmitAddHours} />
                  </div>
                  <div className="mb-3">
                    <label htmlFor="isOnline">Online?</label>
                    <select className="form-control" id="online2" onChange={this.handleChangeOnline}>\
                      <option value=''></option>
                      <option value='true'>Yes</option>
                      <option value='false'>No</option>
                    </select>
                  </div>
                </form>
                <button style={{ 'margin-right': "10px" }} className="btn btn-primary" onClick={this.handleSubmitEditCourse}>Edit</button>
                <button className="btn btn-primary" onClick={() => this.setState({ popUpButtonEditCourse: false })}>
                  Cancel
                </button>
              </Popup>

              <button style={{ 'margin-left': "33px", 'marginBottom': "10px" }} className="btn btn-primary" onClick={() => this.setState({ popUpButtonDeleteCourse: true })}>
                Delete Course
              </button>
              <Popup trigger={this.state.popUpButtonDeleteCourse}>
                <h3>Delete Course</h3>

                <form className="form-floating" onSubmit={this.handleSubmitDeleteCourse}>
                <div className="mb-3">
                    <label htmlFor="course">Course</label>
                    <select className="form-control" id="deleteCourse" onChange={this.handleChangeCourseID}>\
                      <option value='0'></option>
                      {this.state.courses.map((course) => (
                        <option value={course.courseID}>{course.courseName}</option>
                      ))}
                    </select>
                  </div>
                </form>
                <button style={{ 'margin-right': "10px" }} className="btn btn-primary" onClick={this.handleSubmitDeleteCourse}>Delete</button>
                <button className="btn btn-primary" onClick={() => this.setState({ popUpButtonDeleteCourse: false })}>
                  Cancel
                </button>
              </Popup>
              <ul>
                {this.state.semesters.map((semester) => (
                  <div key={semester.semesterID}>
                    <h3>{semester.semesterName}</h3>
                    <h5 className={'nav-item'} >
                      {this.displayCourses(semester.semesterID)}
                    </h5>
                  </div>
                ))}
              </ul>

            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Semesters;

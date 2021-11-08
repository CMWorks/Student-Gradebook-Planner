import React from "react";
import { Link } from "react-router-dom";

// Each elemetn of the second list
function CourseBox(props) {
    return (
        <div>
            <Link type="button" className="btn btn-outline-primary" to="/course" onClick={()=>{props.set({selectedCourseID: props.data.courseID})}}>
                {props.data.courseName}
                {" - creditHours: "}
                {props.data.creditHours}
                {" - isOnline: "}
                {props.data.isOnline ? "true" : "false"}
                {" - grade: "}
                {props.data.grade}
            </Link>
        </div>
    );
}

// Each element of the main list
class SemesterBox extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            semester: this.props.data,
            courses: [],
            hide: true
        }

        this.handleClick = this.handleClick.bind(this);

        this.getCor(this.state.semester.semesterID);
    }

    getCor(semesterID) {
        this.props.server.getAllFromTable('currentCourses', 'semesterID', semesterID).then(retrieve => {
            // retrieve is {success: bool, data: array of objects}
            let data = retrieve.data;
            this.setState({ courses: data });
        })
    }

    handleClick() {
        let chide = !this.state.hide;
        this.setState({ hide: chide });
    }

    render() {
        const data = this.state.courses;
        const set = this.props.set;
        const listCourses = data.map(function (d, idx) {
            return (
                <li key={d.courseID}>
                    <CourseBox
                        data={d}
                        set={set}
                    />
                </li>
            )
        })
        if (this.state.hide) {
            return (
                <div>
                    <button type="button" className="btn btn-dark" onClick={this.handleClick}>
                        {this.props.data.semesterName}
                        {" - gpa: "}
                        {this.props.data.gpa}
                    </button>
                </div>


            );
        } else {
            return (
                <div>
                    <button type="button" className="btn btn-info" onClick={this.handleClick}>
                        {this.props.data.semesterName}
                        {" - gpa: "}
                        {this.props.data.gpa}
                    </button>
                    <ul>
                        {listCourses}
                    </ul>
                </div>


            );
        }
    }
}

// Main semester list
class Semesters extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            semesters: []
        }
        this.getSem();
    }

    getSem() {
        let id = this.props.userData.userID;
        this.props.server.getAllFromTable('semesters', 'userID', id).then(retrieve => {
            // retrieve is {success: bool, data: array of objects}
            let data = retrieve.data;

            this.setState({ semesters: data });
        })
    }

    render() {
        const data = this.state.semesters;
        const server = this.props.server;
        const set = this.props.set;
        const listSemester = data.map(function (d, idx) {
            return (
                <li key={idx}>
                    <SemesterBox
                        data={d}
                        server={server}
                        set={set}
                    />
                </li>)
        })

        return (
            <div className="semesters">
                <div className="container">
                    <h1 className="font-weight-light">Semesters</h1>
                    {listSemester}
                </div>
            </div>
        );
    }
}

export default Semesters;
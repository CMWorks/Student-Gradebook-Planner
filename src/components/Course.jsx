import React from "react";
import AssignmentCategory from "./AssignmentCategory";
import Assignments from "./Assignments";
import Categories from "./Categories";

class Course extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            courses: {},
        }
        this.props.server.getAllFromTable('categories', 'courseID', this.props.selectedCourseID).then(retrieve => {
            // retrieve is {success: bool, data: array of objects}
            return retrieve.data;
        }).then((catData) => {
            this.props.server.getAllFromTable('assignments', 'courseID', this.props.selectedCourseID).then(retrieve => {
                // retrieve is {success: bool, data: array of objects}
                let data = retrieve.data;
                this.setState({ categories: catData, assignments: data });
            })
        })
    }

    render() {
        return (
            <div>
                <h1 className="card card-body mb-3">IT - 279</h1>
                <div className="container">
                    <h4>Category Weight Category Grade</h4>
                    <Categories />
                </div>

            </div >
        )
    }
}

export default Course;
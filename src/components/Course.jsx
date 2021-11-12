import React from "react";
import AssignmentCategory from "./AssignmentCategory";
import Assignments from "./Assignments";
import Categories from "./Categories";
import Popup from "./Popup";
import { useState } from 'react';



class Course extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            courseName: this.props.courseName,
            courseID: this.props.courseID,
            semesterID: this.props.semesterID,
            assignmentCategories: [],
            assignments: [],
            popUpButton: false,
            categoryName: '',
            categoryWeight: 0,
        };
        this.handleChangeCategoryName = this.handleChangeCategoryName.bind(this);
        this.handleChangeCategoryWeight = this.handleChangeCategoryWeight.bind(this);
        this.handleSubmitAddCategory = this.handleSubmitAddCategory.bind(this);

    }

    componentDidMount = async () => {
        this.props.server.getAllFromTable('categories', 'courseID', this.props.courseID).then(retrieve => {
            let success = retrieve.success;
            let data = retrieve.data;

            console.log('success: ' + success);
            this.setState({ assignmentCategories: retrieve.data });
            console.log(this.state.assignmentCategories);
            this.getAssignmentInfo();

        });
    }



    getAssignmentInfo = async () => {
        for (let i = 0; i < this.state.assignmentCategories.length; i++) {
            const response = await this.props.server.getAllFromTable('assignments', 'categoryID', this.state.assignmentCategories[i].categoryID).then(retrieve => {
                let success = retrieve.success;
                let data = retrieve.data;

                console.log('success: ' + success);
                return data;
            })
            this.setState({ assignments: this.state.assignments.concat(response) });
        }
    }

    displayAssignments(categoryID) {
        let array = [];
        for (let m = 0; m < this.state.assignments.length; m++) {
            //   console.log(categoryID);
            //   console.log(this.state.assignments[m].categoryID);
            if (categoryID == this.state.assignments[m].categoryID) {
                array.push(
                    <tr style={{ border: "1px solid  gray", padding: "3px" }}>
                        <th style={{ border: "1px solid  gray", padding: "3px" }}>
                            {this.state.assignments[m].assignmentName}
                        </th>
                        <th style={{ border: "1px solid  gray", padding: "3px" }}>
                            {this.state.assignments[m].pointsReceived}
                        </th>
                        <th style={{ border: "1px solid  gray", padding: "3px" }}>
                            {this.state.assignments[m].totalPoints}
                        </th>
                        <th style={{ border: "1px solid  gray", padding: "3px" }}>
                            {this.state.assignments[m].percentGrade}
                        </th>
                        <th style={{ border: "1px solid  gray", padding: "3px" }}>
                            {this.state.assignments[m].dueDate}
                        </th>
                    </tr>
                );
            }
        }
        return array;
    }


    //This is to add the category
    handleSubmitAddCategory(event) {
        //Create the category object to send
        let Category = {
            categoryID: this.props.server.generateID(), //How should I calculate this?
            categoryName: this.state.categoryName,
            weight: this.state.categoryWeight,
            categoryGrade: 0, //I dont know how I am supposed to calculate this with the function in the python file
            courseID: this.state.courseID,
            semesterID: this.state.semesterID,
            userID: this.props.userData.userID
        }
        if (this.state.categoryName === "" || this.state.categoryWeight === "") {
            event.preventDefault();
            return
        }
        console.log(Category);
        this.props.server.addUserData('categories', Category); //This is not working, getting internal server error
        event.preventDefault();
    }

    handleChangeCategoryName(event) {
        this.setState({ categoryName: event.target.value });
    }

    handleChangeCategoryWeight(event) {
        this.setState({ categoryWeight: event.target.value });
    }


    render() {

        return (
            <div>
                <h1 className="card card-body mb-3">{this.state.courseName}</h1>
                <div className="container">

                    <button style={{ 'margin-left': "33px", 'marginBottom': "10px" }} className="btn btn-primary" onClick={() => this.setState({ popUpButton: true })}>
                        Add Category
                    </button>
                    <Popup trigger={this.state.popUpButton}>
                        <h3>Add Category</h3>
                        <form className="form-floating" onSubmit={this.handleSubmitAddCategory}>
                            <div className="mb-3">
                                <label htmlFor="categoryName">Category Name</label>
                                <input type="text" className="form-control" onChange={this.handleChangeCategoryName} />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="categoryName">Category Weight</label>
                                <input type="number" className="form-control" onChange={this.handleChangeCategoryWeight} />
                            </div>
                        </form>
                        <button style={{ 'margin-right': "10px" }} className="btn btn-primary" onClick={this.handleSubmitAddCategory}>Submit</button>

                        <button className="btn btn-primary" onClick={() => this.setState({ popUpButton: false })}>
                            Cancel
                        </button>
                    </Popup>

                    <ul>
                        {this.state.assignmentCategories.map((categories) => (
                            <div>
                                <table style={{ width: "100%", 'borderCollapse': "collapse" }}>
                                    <tr style={{ border: "1px solid  gray", padding: "3px" }}>
                                        <th style={{ border: "1px solid  gray", padding: "3px" }}>
                                            Gradebook Item
                                        </th>
                                        <th style={{ border: "1px solid  gray", padding: "3px" }}>
                                            Points Received
                                        </th>
                                        <th style={{ border: "1px solid  gray", padding: "3px" }}>
                                            Total Points
                                        </th>
                                        <th style={{ border: "1px solid  gray", padding: "3px" }}>
                                            Percent Grade
                                        </th>
                                        <th style={{ border: "1px solid  gray", padding: "3px" }}>
                                            Due Date
                                        </th>
                                    </tr>
                                    <h4 key={categories.categoryID}>{categories.categoryName}</h4>
                                    {this.displayAssignments(categories.categoryID)}
                                </table>
                            </div>
                        ))}
                    </ul>
                </div>

            </div>
        )
    }
}

export default Course;
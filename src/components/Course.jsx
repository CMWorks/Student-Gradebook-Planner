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
            gradePercent: 0,
            gradeLetter: '',
            totalWeight: 0,
            semesterID: this.props.semesterID,
            categoryID: 0,
            assignmentCategories: [],
            assignments: [],
            popUpButton: false,
            popUpButtonAssignment: false,
            popUpButtonEditCategory: false,
            popUpButtonDeleteCategory: false,
            popUpButtonEditAssignment: false,
            popUpButtonDeleteAssignment: false,
            popUpButtonErrorCategory: false,
            assignmentID: 0,
            categoryName: '',
            categoryWeight: 0,
            assignmentName: '',
            pointsReceived: 0,
            totalPoints: 0,
            dueDate: '',
            isDone: 0,
        };
        this.handleChangeCategoryName = this.handleChangeCategoryName.bind(this);
        this.handleChangeCategoryID = this.handleChangeCategoryID.bind(this);
        this.handleChangeCategoryWeight = this.handleChangeCategoryWeight.bind(this);
        this.handleSubmitAddCategory = this.handleSubmitAddCategory.bind(this);
        this.handleSubmitEditCategory = this.handleSubmitEditCategory.bind(this);
        this.handleSubmitDeleteCategory = this.handleSubmitDeleteCategory.bind(this);
        
        this.handleSubmitDeleteAssignment = this.handleSubmitDeleteAssignment.bind(this);
        this.handleChangeAssignmentID = this.handleChangeAssignmentID.bind(this);
        this.handleChangeAssignmentName = this.handleChangeAssignmentName.bind(this);
        this.handleChangeAssignmentPointsReceived = this.handleChangeAssignmentPointsReceived.bind(this);
        this.handleChangeAssignmentTotalPoints = this.handleChangeAssignmentTotalPoints.bind(this);
        this.handleChangeAssignmentDueDate = this.handleChangeAssignmentDueDate.bind(this);
        this.handleSubmitAddAssignment = this.handleSubmitAddAssignment.bind(this);
        this.handleChangeAssignmentIsDone = this.handleChangeAssignmentIsDone.bind(this);
        this.handleSubmitEditAssignment = this.handleSubmitEditAssignment.bind(this);
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
        this.calculateGrade();
    }

    displayAssignments(categoryID) {
        let array = [];
        for (let m = 0; m < this.state.assignments.length; m++) {
            //   console.log(categoryID);
            //   console.log(this.state.assignments[m].categoryID);
            if (categoryID == this.state.assignments[m].categoryID) {
                array.push(
                    <tr style={{ border: "1px solid  gray", padding: "3px" }}>
                        <th style={{ width: "10vw", border: "1px solid  gray", padding: "3px" }}>
                            {this.state.assignments[m].assignmentName}
                        </th>
                        <th style={{ width: "10vw", border: "1px solid  gray", padding: "3px" }}>
                            {this.state.assignments[m].pointsReceived}
                        </th>
                        <th style={{width: "10vw", border: "1px solid  gray", padding: "3px" }}>
                            {this.state.assignments[m].totalPoints}
                        </th>
                        <th style={{width: "10vw", border: "1px solid  gray", padding: "3px" }}>
                            {this.state.assignments[m].percentGrade.toFixed(2)}
                        </th>
                        <th style={{width: "10vw", border: "1px solid  gray", padding: "3px" }}>
                            {this.state.assignments[m].dueDate}
                        </th>
                    </tr>
                );
            }
        }
        return array;
    }
    
    handleSubmitAddCategory(event) {
        //Create the category object to send
        let Category = {
            categoryID: this.props.server.generateID(), 
            categoryName: this.state.categoryName,
            weight: this.state.categoryWeight,
            categoryGrade: 0, 
            courseID: this.state.courseID,
            semesterID: this.state.semesterID,
            userID: this.props.userData.userID
        }
        let totalWeight = parseInt(this.state.categoryWeight);
        for (let i = 0; i < this.state.assignmentCategories.length; i++){
            totalWeight = totalWeight + this.state.assignmentCategories[i].weight;
        }
        if (this.state.categoryName === "") {
            event.preventDefault();
            document.getElementById("categoryName").classList.add("is-invalid")
            return
        }
        if(this.state.categoryWeight === 0)
        {
            event.preventDefault();
            document.getElementById("categoryWeight").classList.add("is-invalid")
            return
        }
        if(totalWeight > 100)
        {
            event.preventDefault();
            document.getElementById("categoryWeight").classList.add("is-invalid")
            this.setState({popUpButtonErrorCategory: true})
            return
        }
        this.props.server.addUserData('categories', Category);
        this.setState({ popUpButton: false });
        this.calculateGrade();
        event.preventDefault();
    }

    handleSubmitEditCategory(event) {
        //Create the category object to send
        let Category = {
            categoryID: this.state.categoryID, 
            categoryName: this.state.categoryName,
            weight: this.state.categoryWeight,
            categoryGrade: 0, 
            courseID: this.state.courseID,
            semesterID: this.state.semesterID,
            userID: this.props.userData.userID
        }
        let totalWeight = parseInt(this.state.categoryWeight);
        for (let i = 0; i < this.state.assignmentCategories.length; i++){
            totalWeight = totalWeight + this.state.assignmentCategories[i].weight;
        }
        if (this.state.categoryName === "") {
            event.preventDefault();
            document.getElementById("categoryName1").classList.add("is-invalid")
            return
        }
        if(this.state.categoryWeight === 0)
        {
            event.preventDefault();
            document.getElementById("categoryWeight1").classList.add("is-invalid")
            return
        }
        if(totalWeight > 100)
        {
            event.preventDefault();
            document.getElementById("categoryWeight1").classList.add("is-invalid")
            this.setState({popUpButtonErrorCategory: true})
            return
        }
        // console.log(Category);
        this.props.server.updateUserData('categories', this.state.categoryID ,Category);
        this.setState({ popUpButtonEditCategory: false });
        this.calculateGrade();
        event.preventDefault();
    }

    handleSubmitDeleteCategory(event) {
        if (this.state.categoryID === 0) {
            event.preventDefault();
            document.getElementById("deleteCategory").classList.add("is-invalid")
            return
        }
        this.props.server.deleteUserData('categories', this.state.categoryID);
        this.setState({popUpButtonDeleteCategory: false});
        this.calculateGrade();
        event.preventDefault();
    }

    handleSubmitDeleteAssignment(event) {
        if (this.state.assignmentID === 0) {
            event.preventDefault();
            document.getElementById("assignmentIDDelete").classList.add("is-invalid")
            return
        }
        this.props.server.deleteUserData('assignments', this.state.assignmentID);
        this.setState({popUpButtonDeleteAssignment: false});
        this.calculateGrade();
        event.preventDefault();
    }

    handleChangeCategoryID(event) {
        
        this.setState({ categoryID: event.target.value });
    }

    handleChangeAssignmentID(event) {
        this.setState({ assignmentID: event.target.value });
    }

    handleChangeCategoryName(event) {
        this.setState({ categoryName: event.target.value });
    }

    handleChangeCategoryWeight(event) {
        this.setState({ categoryWeight: event.target.value });
    }

    handleSubmitAddAssignment(event) {
        //Create the assignment object to send
        let Assignment = {
            assignmentID: this.props.server.generateID(), 
            assignmentName: this.state.assignmentName,
            pointsReceived: this.state.pointsReceived,
            totalPoints: this.state.totalPoints,
            percentGrade: (this.state.pointsReceived/this.state.totalPoints)*100,
            dueDate: this.state.dueDate, 
            isDone: this.state.isDone,
            categoryID:  this.state.categoryID,
            courseID: this.state.courseID,
            semesterID: this.state.semesterID,
            userID: this.props.userData.userID
        }
        // console.log(Assignment);
        if (this.state.assignmentName === "") {
            event.preventDefault();
            document.getElementById("assignmentNameAdd").classList.add("is-invalid")
            return
        }
        if(this.state.categoryID === 0)
        {
            event.preventDefault();
            document.getElementById("categoryIDAdd").classList.add("is-invalid")
            return
        }
        if(this.state.totalPoints === 0)
        {
            event.preventDefault();
            document.getElementById("totalPointsAdd").classList.add("is-invalid")
            return
        }
        this.props.server.addUserData('assignments', Assignment);
        this.setState({ popUpButtonAssignment: false });
        this.calculateGrade();
        event.preventDefault();
    }
    
    handleSubmitEditAssignment(event) {
        let Assignment = {
            assignmentID: this.state.assignmentID, 
            assignmentName: this.state.assignmentName,
            pointsReceived: this.state.pointsReceived,
            totalPoints: this.state.totalPoints,
            percentGrade: (this.state.pointsReceived/this.state.totalPoints)*100,
            dueDate: this.state.dueDate, 
            isDone: this.state.isDone,
            categoryID:  this.state.categoryID,
            courseID: this.state.courseID,
            semesterID: this.state.semesterID,
            userID: this.props.userData.userID
        }
        // console.log(Assignment);
        if (this.state.assignmentID === 0) {
            event.preventDefault();
            document.getElementById("assignmentIDEdit").classList.add("is-invalid")
            return
        }
        if (this.state.assignmentName === "") {
            event.preventDefault();
            document.getElementById("assignmentNameEdit").classList.add("is-invalid")
            return
        }
        if(this.state.categoryID === 0)
        {
            event.preventDefault();
            document.getElementById("categoryIDEdit").classList.add("is-invalid")
            return
        }
        if(this.state.totalPoints === 0)
        {
            event.preventDefault();
            document.getElementById("totalPointsEdit").classList.add("is-invalid")
            return
        }
        this.props.server.updateUserData('assignments', this.state.assignmentID, Assignment);
        this.setState({ popUpButtonEditAssignment: false });
        this.calculateGrade();
        event.preventDefault();
    }

    handleChangeAssignmentName(event) {
        this.setState({ assignmentName: event.target.value });
    }

    handleChangeAssignmentPointsReceived(event) {
        this.setState({ pointsReceived: event.target.value });
    }

    handleChangeAssignmentTotalPoints(event) {
        this.setState({ totalPoints: event.target.value });
    }

    handleChangeAssignmentDueDate(event) {
        this.setState({ dueDate: event.target.value });
    }

    handleChangeAssignmentIsDone(event) {
        this.setState({ isDone: event.target.value });
    }

    calculateGrade(){
        let percentGradeTotal = 100;
        let percentGradeCat = 0;
        let totalCatPoints = 0;
        let earnedCatPoints = 0;
        let categoryID = 0;
        let categoryWeight = 0;
        for (let i = 0; i < this.state.assignmentCategories.length; i++){
            totalCatPoints = 0;
            earnedCatPoints = 0;
            categoryID = this.state.assignmentCategories[i].categoryID;
            categoryWeight = this.state.assignmentCategories[i].weight;
            for (let m = 0; m < this.state.assignments.length; m++) {
                if (categoryID == this.state.assignments[m].categoryID) {
                    totalCatPoints = totalCatPoints + this.state.assignments[m].totalPoints;
                    earnedCatPoints = earnedCatPoints + this.state.assignments[m].pointsReceived;
                }
            }
            percentGradeCat = (earnedCatPoints/totalCatPoints);
            percentGradeCat = percentGradeCat*categoryWeight;
            if(!isNaN(percentGradeCat))
            {
                percentGradeTotal = percentGradeTotal - (categoryWeight - percentGradeCat);
            }
        }
        this.setState({gradePercent: percentGradeTotal});
        if(percentGradeTotal >= 90)
        {
            this.setState({gradeLetter: 'A'});
        }
        else if(percentGradeTotal >= 80)
        {
            this.setState({gradeLetter: 'B'});
        }
        else if(percentGradeTotal >= 70)
        {
            this.setState({gradeLetter: 'C'});
        }
        else if(percentGradeTotal >= 60)
        {
            this.setState({gradeLetter: 'D'});
        }
        else
        {
            this.setState({gradeLetter: 'F'});
        }
    }

    render() {
        return (
            <div  style={{overflow: "auto", height: "770px"}}>
                <h1 className="card card-body mb-3">{this.state.courseName} - {this.state.gradeLetter} ({this.state.gradePercent.toFixed(2)}%)</h1>
                <div className="container" >

                    <button style={{ 'margin-left': "33px", 'marginBottom': "10px" }} className="btn btn-primary" onClick={() => this.setState({ popUpButton: true })}>
                        Add Category
                    </button>
                    
                    <Popup trigger={this.state.popUpButton}>
                        <h3>Add Category</h3>
                        <form className="form-floating" onSubmit={this.handleSubmitAddCategory}>
                            <div className="mb-3">
                                <label htmlFor="categoryName">Category Name</label>
                                <input type="text" className="form-control" id="categoryName" onChange={this.handleChangeCategoryName} />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="categoryWeight">Category Weight</label>
                                <input type="number" className="form-control" id="categoryWeight" onChange={this.handleChangeCategoryWeight} />
                            </div>
                        </form>
                        <button style={{ 'margin-right': "10px" }} className="btn btn-primary" onClick={this.handleSubmitAddCategory}>Submit</button>

                        <button className="btn btn-primary" onClick={() => this.setState({ popUpButton: false })}>
                            Cancel
                        </button>
                    </Popup>

                    <button style={{ 'margin-left': "33px", 'marginBottom': "10px" }} className="btn btn-primary" onClick={() => this.setState({ popUpButtonEditCategory: true })}>
                        Edit Category
                    </button>
                    <Popup trigger={this.state.popUpButtonEditCategory}>
                        <h3>Edit Category</h3>
                        
                        <form className="form-floating" onSubmit={this.handleSubmitEditCategory}>
                            <div className="mb-3">
                                <label htmlFor="category">Category</label>
                                <select className="form-control" onChange={this.handleChangeCategoryID}>\
                                    <option value=''></option>
                                    {this.state.assignmentCategories.map((categories) => (
                                            <option value={categories.categoryID}>{categories.categoryName}</option>
                                        ))}
                                </select>
                            </div>
                            <div className="mb-3">
                                <label htmlFor="categoryName">Category Name</label>
                                <input type="text" className="form-control" id="categoryName1" onChange={this.handleChangeCategoryName} />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="categoryWeight">Category Weight</label>
                                <input type="number" className="form-control" id="categoryWeight1" onChange={this.handleChangeCategoryWeight} />
                            </div>
                        </form>
                        <button style={{ 'margin-right': "10px" }} className="btn btn-primary" onClick={this.handleSubmitEditCategory}>Submit</button>

                        <button className="btn btn-primary" onClick={() => this.setState({ popUpButtonEditCategory: false })}>
                            Cancel
                        </button>
                    </Popup>

                    <button style={{ 'margin-left': "33px", 'marginBottom': "10px" }} className="btn btn-primary" onClick={() => this.setState({ popUpButtonDeleteCategory: true })}>
                        Delete Category
                    </button>
                    <Popup trigger={this.state.popUpButtonDeleteCategory}>
                        <h3>Delete Category</h3>
                        
                        <form className="form-floating" onSubmit={this.handleSubmitDeleteCategory}>
                            <div className="mb-3">
                                <label htmlFor="category">Category</label>
                                <select className="form-control" id="deleteCategory" onChange={this.handleChangeCategoryID}>\
                                    <option value=''></option>
                                    {this.state.assignmentCategories.map((categories) => (
                                            <option value={categories.categoryID}>{categories.categoryName}</option>
                                        ))}
                                </select>
                            </div>
                        </form>
                        <button style={{ 'margin-right': "10px" }} className="btn btn-primary" onClick={this.handleSubmitDeleteCategory}>Submit</button>

                        <button className="btn btn-primary" onClick={() => this.setState({ popUpButtonDeleteCategory: false })}>
                            Cancel
                        </button>
                    </Popup>

                    <button style={{ 'margin-left': "33px", 'marginBottom': "10px" }} className="btn btn-primary" onClick={() => this.setState({ popUpButtonAssignment: true })}>
                        Add Assignment
                    </button>
                    <Popup trigger={this.state.popUpButtonAssignment}>
                        <h3>Add Assignment</h3>
                        <form className="form-floating" onSubmit={this.handleSubmitAddAssignment}>
                            <div className="mb-3">
                                <label htmlFor="assignmentName">Assignment Name</label>
                                <input type="text" className="form-control" id="assignmentNameAdd" onChange={this.handleChangeAssignmentName} />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="pointsReceived">Points Received</label>
                                <input type="number" className="form-control" onChange={this.handleChangeAssignmentPointsReceived} />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="totalPoints">Total Points</label>
                                <input type="number" className="form-control" id="totalPointsAdd" onChange={this.handleChangeAssignmentTotalPoints} />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="dueDate">Due Date</label>
                                <input type="date" className="form-control" onChange={this.handleChangeAssignmentDueDate} />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="isDone">Completed?  </label>
                                <select className="form-control" onChange={this.handleChangeCategoryID}>\
                                    <option value=''></option>
                                    <option value='1'>yes</option>
                                    <option value='0'>no</option>
                                </select>
                            </div>
                            <div className="mb-3">
                                <label htmlFor="category">Category</label>
                                <select className="form-control" id="categoryIDAdd" onChange={this.handleChangeCategoryID}>\
                                    <option value=''></option>
                                    {this.state.assignmentCategories.map((categories) => (
                                            <option value={categories.categoryID}>{categories.categoryName}</option>
                                        ))}
                                </select>
                            </div>
                        </form>
                        <button style={{ 'margin-right': "10px" }} className="btn btn-primary" onClick={this.handleSubmitAddAssignment}>Submit</button>

                        <button className="btn btn-primary" onClick={() => this.setState({ popUpButtonAssignment: false })}>
                            Cancel
                        </button>
                    </Popup>

                    <button style={{ 'margin-left': "33px", 'marginBottom': "10px" }} className="btn btn-primary" onClick={() => this.setState({ popUpButtonEditAssignment: true })}>
                        Edit Assignment
                    </button>
                    <Popup trigger={this.state.popUpButtonEditAssignment}>
                        <h3>Edit Assignment</h3>
                        <form className="form-floating" onSubmit={this.handleSubmitEditAssignment}>
                            <div className="mb-3">
                                <label htmlFor="category">Assignments</label>
                                <select className="form-control" id="assignmentIDEdit" onChange={this.handleChangeAssignmentID}>
                                    <option value=''></option>
                                    {this.state.assignments.map((assignment) => (
                                            <option value={assignment.assignmentID}>{assignment.assignmentName}</option>
                                        ))}
                                </select>
                            </div>
                            <div className="mb-3">
                                <label htmlFor="assignmentName">Assignment Name</label>
                                <input type="text" className="form-control" id="assignmentNameEdit" onChange={this.handleChangeAssignmentName} />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="pointsReceived">Points Received</label>
                                <input type="number" className="form-control" onChange={this.handleChangeAssignmentPointsReceived} />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="totalPoints">Total Points</label>
                                <input type="number" className="form-control" id="totalPointsEdit" onChange={this.handleChangeAssignmentTotalPoints} />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="dueDate">Due Date</label>
                                <input type="date" className="form-control" onChange={this.handleChangeAssignmentDueDate} />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="isDone">Completed?  </label>
                                <select className="form-control" onChange={this.handleChangeCategoryID}>\
                                    <option value=''></option>
                                    <option value='1'>yes</option>
                                    <option value='0'>no</option>
                                </select>
                            </div>
                            <div className="mb-3">
                                <label htmlFor="category">Category</label>
                                <select className="form-control" id="categoryIDEdit" onChange={this.handleChangeCategoryID}>\
                                    <option value=''></option>
                                    {this.state.assignmentCategories.map((categories) => (
                                            <option value={categories.categoryID}>{categories.categoryName}</option>
                                        ))}
                                </select>
                            </div>
                        </form>
                        <button style={{ 'margin-right': "10px" }} className="btn btn-primary" onClick={this.handleSubmitEditAssignment}>Submit</button>

                        <button className="btn btn-primary" onClick={() => this.setState({ popUpButtonEditAssignment: false })}>
                            Cancel
                        </button>
                    </Popup>

                    <button style={{ 'margin-left': "33px", 'marginBottom': "10px" }} className="btn btn-primary" onClick={() => this.setState({ popUpButtonDeleteAssignment: true })}>
                        Delete Assignment
                    </button>
                    <Popup trigger={this.state.popUpButtonDeleteAssignment}>
                        <h3>Delete Assignment</h3>
                        
                        <form className="form-floating"  onSubmit={this.handleSubmitDeleteAssignment}>
                            <div className="mb-3">
                                <label htmlFor="category">Assignment</label>
                                <select className="form-control" id="assignmentIDDelete" onChange={this.handleChangeAssignmentID}>\
                                    <option value=''></option>
                                    {this.state.assignments.map((assignment) => (
                                            <option value={assignment.assignmentID}>{assignment.assignmentName}</option>
                                        ))}
                                </select>
                            </div>
                        </form>
                        <button style={{ 'margin-right': "10px" }} className="btn btn-primary" onClick={this.handleSubmitDeleteAssignment}>Submit</button>

                        <button className="btn btn-primary" onClick={() => this.setState({ popUpButtonDeleteAssignment: false })}>
                            Cancel
                        </button>
                    </Popup>

                    <Popup trigger={this.state.popUpButtonErrorCategory}>
                        <h3>Error</h3>
                        <p>Total category weights cannot be greater than 100.</p>
                        <button className="btn btn-primary" onClick={() => this.setState({ popUpButtonErrorCategory: false })}>
                            Ok
                        </button>
                    </Popup>
                    <hr />
                    <div>
                    <table style={{ width: "100%", 'border-collapse': "collapse" }}>
                        <tr style={{ border: "1px solid  gray", padding: "3px" }}>
                            <th style={{width: "10vw", border: "1px solid  gray", padding: "3px" }}>
                                Gradebook Item
                            </th>
                            <th style={{width: "10vw", border: "1px solid  gray", padding: "3px" }}>
                                Points Received
                            </th>
                            <th style={{width: "10vw", border: "1px solid  gray", padding: "3px" }}>
                                Total Points
                            </th>
                            <th style={{width: "10vw", border: "1px solid  gray", padding: "3px" }}>
                                Percent Grade
                            </th>
                            <th style={{width: "10vw", border: "1px solid  gray", padding: "3px" }}>
                                Due Date
                            </th>
                        </tr>
                    </table>
                    </div>
                        {this.state.assignmentCategories.map((categories) => (
                            <div style={{ width: "100%"}}>
                                <table style={{ width: "100%", 'borderCollapse': "collapse" }}>
                                    <h4 key={categories.categoryID}>{categories.categoryName}  -  {categories.weight}</h4>
                                    {this.displayAssignments(categories.categoryID)}
                                </table>
                            </div>
                        ))}
                </div>

            </div>
        )
    }
}

export default Course;
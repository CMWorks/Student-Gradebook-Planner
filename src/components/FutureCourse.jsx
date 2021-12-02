import React from "react";
import AssignmentCategory from "./AssignmentCategory";
import Assignments from "./Assignments";
import Categories from "./Categories";
import Popup from "./Popup";
import { useState } from 'react';

class FutureCourse extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            userID: this.props.userData.userID,
            courseID: 0,
            futureCourses: [],
            courseName: '',
            creditHours: 0,
            plannedSemester: '',
            popUpButton: false,
            popUpButtonEditFutureCourse: false,
            popUpButtonDeleteFutureCourse:false,
        }; //State
        this.handleSubmitAddFutureCourse = this.handleSubmitAddFutureCourse.bind(this);        // this.handleChangeCourseName = this.handleChangeCourseName.bind(this);
        this.handleSubmitEditFutureCourse = this.handleSubmitEditFutureCourse.bind(this);
        this.handleSubmitDeleteFutureCourse = this.handleSubmitDeleteFutureCourse.bind(this);

        this.handleChangeFutureCourseID = this.handleChangeFutureCourseID.bind(this);
        this.handleChangeFutureCourseName = this.handleChangeFutureCourseName.bind(this);
        this.handleChangeCreditHours = this.handleChangeCreditHours.bind(this);
        this.handleChangePlannedSemester = this.handleChangePlannedSemester.bind(this);
    
    
    
    
    } //Constructor
    
    componentDidMount = async () =>{
        this.props.server.getAllFromTable('futureCourses', 'userID', this.props.userData.userID).then(retrieve => {
            let success = retrieve.success;
            let data = retrieve.data;

            console.log('success ' + success);
            console.log('Data: ' + data);
            this.setState({futureCourses: retrieve.data});
            console.log(this.state.futureCourses);
            
        });
    }

    displayFutureCourses(){
        let array = [];
        console.log('Length' + this.state.futureCourses.length);
        for(let m = 0; m < this.state.futureCourses.length; m++){
            //Possible sort by planned semseter

            array.push(
                <tr style={{ border: "1px solid  gray", padding: "3px"}}>
                    <th style={{width: "10vw", border: "1px solid  gray", padding: "3px"}}>
                        {this.state.futureCourses[m].plannedSemester}
                    </th>
                    <th style={{width: "10vw", border: "1px solid  gray", padding: "3px"}}>
                        {this.state.futureCourses[m].courseName}
                    </th>
                    <th style={{width: "10vw", border: "1px solid  gray", padding: "3px"}}>
                        {this.state.futureCourses[m].creditHours}
                    </th>
                </tr>
            );

        }
        return array;
    }

    handleChangeFutureCourseName(event) {
        this.setState({ courseName: event.target.value });
    }

    handleChangeCreditHours(event) {
        this.setState({ creditHours: event.target.value });
    }

    handleChangePlannedSemester(event) {
        this.setState({ plannedSemester: event.target.value });
    }

    handleChangeFutureCourseID(event){
        this.setState({courseID : event.target.value})
    }
    handleSubmitAddFutureCourse(event) {
        //Create the category object to send
        let FutureCourse = {
            courseID: this.props.server.generateID(), 
            courseName: this.state.courseName,
            creditHours: this.state.creditHours,
            plannedSemester: this.state.plannedSemester,
            userID: this.props.userData.userID
        }
        
        if (this.state.courseName === "") {
            event.preventDefault();
            document.getElementById("courseName").classList.add("is-invalid")
            return
        }
        if(this.state.creditHours === 0)
        {
            event.preventDefault();
            document.getElementById("creditHours").classList.add("is-invalid")
            return
        }
        if(this.state.plannedSemester === '')
        {
            event.preventDefault();
            document.getElementById("plannedSemester").classList.add("is-invalid")
            return
        }
        console.log(FutureCourse);
        this.props.server.addUserData('futureCourses', FutureCourse);
        this.setState({ popUpButton: false });
        event.preventDefault();
    }

    handleSubmitEditFutureCourse(event) {
        //Create the category object to send
        let FutureCourse = {
            courseID: this.state.courseID,
            courseName: this.state.courseName,
            creditHours: this.state.creditHours,
            plannedSemester: this.state.plannedSemester,
            userID: this.props.userData.userID
        }
        
        if (this.state.courseName === "") {
            event.preventDefault();
            document.getElementById("courseName").classList.add("is-invalid")
            return
        }
        if(this.state.creditHours === 0)
        {
            event.preventDefault();
            document.getElementById("creditHours").classList.add("is-invalid")
            return
        }
        if(this.state.plannedSemester === '')
        {
            event.preventDefault();
            document.getElementById("plannedSemester").classList.add("is-invalid")
            return
        }
        // console.log(Category);
        this.props.server.updateUserData('futureCourses', this.state.courseID ,FutureCourse);
        this.setState({ popUpButtonEditFutureCourse: false });
        event.preventDefault();
        
    }

    handleSubmitDeleteFutureCourse(event) {
        if (this.state.courseID === 0) {
            event.preventDefault();
            document.getElementById("deleteFutureCourse").classList.add("is-invalid")
            return
        }
        this.props.server.deleteUserData('futureCourses', this.state.courseID);
        this.setState({popUpButtonDeleteFutureCourse: false});
        event.preventDefault();
    }

    render() {
        return (
            <div  style={{overflow: "auto", height: "770px"}}>
                <h1 className="card card-body mb-3">Planned Courses</h1>
                <div className="container" >

                    <button style={{ 'margin-left': "33px", 'marginBottom': "10px" }} className="btn btn-primary" onClick={() => this.setState({ popUpButton: true })}>
                        Add Planned Course
                    </button>
                    
                    <Popup trigger={this.state.popUpButton}>
                        <h3>Add Planned Course</h3>
                        <form className="form-floating" onSubmit={this.handleSubmitAddFutureCourse}>
                            <div className="mb-3">
                                <label htmlFor="courseName">Course Name</label>
                                <input type="text" className="form-control" id="courseName" onChange={this.handleChangeFutureCourseName} />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="plannedSemester">Planned Semester</label>
                                <input type="text" className="form-control" id="plannedSemester" onChange={this.handleChangePlannedSemester} />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="creditHours">Credit Hours</label>
                                <input type="number" className = "form-control" id= "creditHours" onChange={this.handleChangeCreditHours}/>
                            </div>
                        </form>
                        <button style={{ 'margin-right': "10px" }} className="btn btn-primary" onClick={this.handleSubmitAddFutureCourse}>Submit</button>

                        <button className="btn btn-primary" onClick={() => this.setState({ popUpButton: false })}>
                            Cancel
                        </button>
                    </Popup> 

                    <button style={{ 'margin-left': "33px", 'marginBottom': "10px" }} className="btn btn-primary" onClick={() => this.setState({ popUpButtonEditFutureCourse: true })}>
                        Edit Planned Course
                    </button>
                    <Popup trigger={this.state.popUpButtonEditFutureCourse}>
                        <h3>Edit Planned Course</h3>
                        
                        <form className="form-floating" onSubmit={this.handleSubmitEditFutureCourse}>
                            <div className="mb-3">
                                <label htmlFor="category">Category</label>
                                <select className="form-control" onChange={this.handleChangeFutureCourseID}>\
                                    <option value=''></option>
                                    {this.state.futureCourses.map((futureCourse) => (
                                            <option value={futureCourse.courseID}>{futureCourse.courseName}</option>
                                        ))}
                                </select>
                            </div>
                            <div className="mb-3">
                                <label htmlFor="courseName">Course Name</label>
                                <input type="text" className="form-control" id="courseName" onChange={this.handleChangeFutureCourseName} />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="creditHours">Credit Hours</label>
                                <input type="number" className="form-control" id="creditHours" onChange={this.handleChangeCreditHours} />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="plannedSemester">Planned Semester</label>
                                <input type="text" className="form-control" id="plannedSemester" onChange={this.handleChangePlannedSemester} />
                            </div>
                        </form>
                        <button style={{ 'margin-right': "10px" }} className="btn btn-primary" onClick={this.handleSubmitEditFutureCourse}>Submit</button>

                        <button className="btn btn-primary" onClick={() => this.setState({ popUpButtonEditFutureCourse: false })}>
                            Cancel
                        </button>
                    </Popup>

                    <button style={{ 'margin-left': "33px", 'marginBottom': "10px" }} className="btn btn-primary" onClick={() => this.setState({ popUpButtonDeleteFutureCourse: true })}>
                        Delete Planned Course
                    </button>
                    <Popup trigger={this.state.popUpButtonDeleteFutureCourse}>
                        <h3>Delete Planned Course</h3>
                        
                        <form className="form-floating" onSubmit={this.handleSubmitDeleteFutureCourse}>
                            <div className="mb-3">
                                <label htmlFor="futureCourse">Planned Course</label>
                                <select className="form-control" id="deleteFutureCourse" onChange={this.handleChangeFutureCourseID}>\
                                    <option value=''></option>
                                    {this.state.futureCourses.map((futureCourse) => (
                                            <option value={futureCourse.courseID}>{futureCourse.courseName}</option>
                                        ))}
                                </select>
                            </div>
                        </form>
                        <button style={{ 'margin-right': "10px" }} className="btn btn-primary" onClick={this.handleSubmitDeleteFutureCourse}>Submit</button>

                        <button className="btn btn-primary" onClick={() => this.setState({ popUpButtonDeleteFutureCourse: false })}>
                            Cancel
                        </button>
                    </Popup>
                    <hr />
                    <div>
                    <table style={{ width: "100%", 'border-collapse': "collapse" }}>
                        <tr style={{ border: "1px solid  gray", padding: "3px" }}>
                            <th style={{width: "10vw", border: "1px solid  gray", padding: "3px" }}>
                                Planned Semseter
                            </th>
                            <th style={{width: "10vw", border: "1px solid  gray", padding: "3px" }}>
                                Course Name
                            </th>
                            <th style={{width: "10vw", border: "1px solid  gray", padding: "3px" }}>
                                Credit Hours
                            </th>
                        </tr>
                    </table>
                    </div>
                            <div style={{ width: "100%"}}>
                                <table style={{ width: "100%", 'borderCollapse': "collapse" }}>
                                    {this.displayFutureCourses()}
                                </table>
                            </div>
                </div>

            </div>
        )
    }

}//Class

export default FutureCourse;
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
            userID: this.props.userID,
            futureCourses: [],
            popUpButtonAddFutureCourse: false,
            popUpButtonEditFutureCourse: false,
            popUpButtonDeleteFutureCourse:false,
        }; //State

        // this.handleChangeCourseName = this.handleChangeCourseName.bind(this);
        // this.handleChangeCourseID = this.handleChangeCourseID.bind(this);
        // this.handleChangeCreditHours = this.handleChangeCreditHours.bind(this);
        // this.handleChangedPlannedSemester = this.handleChangedPlannedSemester(this);
        
        
        // this.handleAddCourse = this.handleAddCourse.bind(this)
        // this.handleDeleteCourse
    
    
    
    
    } //Constructor
    
    componentDidMount = async () =>{
        this.props.server.getAllFromTable('futureCourse', 'userID', this.props.userID).then(retrieve => {
            let success = retrieve.success;
            let data = retrieve.data;

            console.log('success ' + success);
            this.setState({futureCourses: data});
            console.log(this.state.futureCourses);
            
        });
    }

    displayFutureCourses(){
        let array = [];
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


    render() {
        return (
            <div  style={{overflow: "auto", height: "770px"}}>
                <h1 className="card card-body mb-3"></h1>
                <div className="container" >

                    <button style={{ 'margin-left': "33px", 'marginBottom': "10px" }} className="btn btn-primary" onClick={() => this.setState({ popUpButton: true })}>
                        Add Planned Course
                    </button>
                    
                    {/* <Popup trigger={this.state.popUpButton}>
                        <h3>Add Planned Course</h3>
                        <form className="form-floating" onSubmit={this.handleSubmitAddCategory}>
                            <div className="mb-3">
                                <label htmlFor="futureCourseName">Course Name</label>
                                <input type="text" className="form-control" id="futureCourseName" onChange={this.handleChangeFutureCourseName} />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="plannedSemester">Planned Semester</label>
                                <input type="text" className="form-control" id="categoryWeight" onChange={this.handleChangePlannedSemester} />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="creditHours">Credit Hours</label>
                                <input type="number" className = "form-control" id= "creditHours" onChange={this.handleChangeCreditHours}/>
                            </div>
                        </form>
                        <button style={{ 'margin-right': "10px" }} className="btn btn-primary" onClick={this.handleSubmitAddCategory}>Submit</button>

                        <button className="btn btn-primary" onClick={() => this.setState({ popUpButton: false })}>
                            Cancel
                        </button>
                    </Popup>  */}
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
                        {this.state.futureCourses.map(() => (
                            <div style={{ width: "100%"}}>
                                <table style={{ width: "100%", 'borderCollapse': "collapse" }}>
                                    <h4 key={this.userID}>{this.futureCourse}</h4>
                                    {this.displayFutureCourses()}
                                </table>
                            </div>
                        ))}
                </div>

            </div>
        )
    }

}//Class

export default FutureCourse;
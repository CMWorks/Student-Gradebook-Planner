import React from "react";
import AssignmentCategory from "./AssignmentCategory";
import Assignments from "./Assignments";
import Categories from "./Categories";

class Course extends React.Component
{
    

    render() {
        return (
        <div>
            <h1 className="card card-body mb-3">IT - 279</h1>
            <div className="container">
                <h4>Category Weight Category Grade</h4>
                <Categories />
            </div>
            
        </div>
        )
    }
}

export default Course;
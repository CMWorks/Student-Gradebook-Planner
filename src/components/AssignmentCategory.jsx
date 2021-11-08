import React, { Component } from 'react'
import Assignment from './Assignment';

class AssignmentCategory extends Component {
    constructor(props)
    {
        super(props);
    }



    render() {
        const { category } = this.props;

        return (
            <div>
                <div className="card card-body mb-3">
                    <h4>{category.name} {category.weight} {category.grade}</h4>
                    <ul className="list-group">
                        <li className="list-group-item"><Assignment assignmentName="Exam1" pointsReceived="10" pointsTotal="12" percentGrade="80"/></li>
                    </ul>
                </div>
            </div>
        )
    }
}

export default AssignmentCategory;

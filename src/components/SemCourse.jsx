import React, { Component } from 'react'

class SemCourse extends Component {
    constructor(props)
    {
        super(props);
    }



    render() {
        const { course } = this.props;

        return (
            <div>
                <div className="card card-body mb-3">
                    <h4>{course.name}</h4>
                </div>
            </div>
        )
    }
}

export default SemCourse;
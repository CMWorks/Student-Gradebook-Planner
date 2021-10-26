import React, { Component } from 'react'

class Assignments extends Component {
    constructor()
    {
        super();
        this.state = {
            assignments: [
                {
                    name: 'Exam1',
                    pointsReceived: 10,
                    totalPoints: 10,
                    grade: 100
                },
                {
                    name: 'Exam2',
                    pointsReceived: 10,
                    totalPoints: 10,
                    grade: 100
                }
            ]
        }
    }

    render() {
        return (
            <div>
                
            </div>
        )
    }
}

export default Assignments;

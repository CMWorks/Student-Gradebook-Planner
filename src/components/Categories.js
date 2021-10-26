import React, { Component } from 'react'
import AssignmentCategory from './AssignmentCategory';

class Categories extends Component {
    constructor()
    {
        super();
        this.state = {
            categories: [
                {
                    name: 'Exams',
                    weight: 50,
                    grade: 100
                },
                {
                    name: 'Homework',
                    weight: 50,
                    grade: 100
                }
            ]
        }
    }

    render() {
        const { categories } = this.state;

        return (
            <div>
                {categories.map(category => 
                    <AssignmentCategory key={category.name} category={category}/>
                )}
            </div>
        );
    }
}

export default Categories;
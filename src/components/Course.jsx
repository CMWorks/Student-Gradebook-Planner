import React from "react";
import AssignmentCategory from "./AssignmentCategory";
import Assignments from "./Assignments";
import Categories from "./Categories";


class Course extends React.Component
{
    constructor(props)
    {
        super(props);
        this.state = {
            courseName: this.props.courseName,
            courseID: this.props.courseID,
            assignmentCategories: [],
            assignments: []
        }
        
    }

    componentDidMount = async () =>
    {
          this.props.server.getAllFromTable('categories', 'courseID', this.props.courseID).then(retrieve => {
              let success = retrieve.success;
              let data = retrieve.data;
  
              console.log('success: ' + success);
              this.setState({assignmentCategories: retrieve.data});
              console.log(this.state.assignmentCategories);
              this.getAssignmentInfo();
              
          });
    }


    
    getAssignmentInfo = async () =>
    {
      for(let i = 0; i < this.state.assignmentCategories.length; i++)
      {
        const response = await this.props.server.getAllFromTable('assignments', 'categoryID', this.state.assignmentCategories[i].categoryID).then(retrieve => {
              let success = retrieve.success;
              let data = retrieve.data;

              console.log('success: ' + success);
              return data;
            })
            this.setState({assignments: this.state.assignments.concat(response)});
            // console.log(this.state.assignments);
      }
    }

    displayAssignments(categoryID) {
        let array = [];
        for(let m = 0; m < this.state.assignments.length; m++)
        {
        //   console.log(categoryID);
        //   console.log(this.state.assignments[m].categoryID);
          if(categoryID == this.state.assignments[m].categoryID)
          {
              array.push(
                <ul>
                  {this.state.assignments[m].assignmentName}
                </ul>
              );
          }
        }
        return array;
      }

    render() {
        // this.getting();
        
        return (
        <div>
            <h1 className="card card-body mb-3">{this.state.courseName}</h1>
            <div className="container">
                <h4>Category Weight Category Grade</h4>
                <ul>
                  {this.state.assignmentCategories.map((categories) =>  (
                    <div>
                      <h4 key={categories.categoryID}>{categories.categoryName}</h4>
                      <ul className={'nav-item'} >
                      {this.displayAssignments(categories.categoryID)}
                      </ul>
                    </div>
                  ))}
                </ul>
            </div>
            
        </div>
        )
    }
}

export default Course;
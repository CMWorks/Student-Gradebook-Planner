import React from "react";
import { Link } from "react-router-dom";

class Semesters extends React.Component {
    constructor(props)
    {
      super(props);
      this.state = {
        semesters: [],
        courses: []
      }
    }


    
    componentDidMount = async () =>
    {
      let id = this.props.userData.userID;
          this.props.server.getAllFromTable('semesters', 'userID', id).then(retrieve => {
              let success = retrieve.success;
              let data = retrieve.data;
  
              console.log('success: ' + success);
              this.setState({semesters: retrieve.data});
              this.getCourseInfo();
          });
    }

    getCourseInfo = async () =>
    {
      for(let i = 0; i < this.state.semesters.length; i++)
      {
        const response = await this.props.server.getAllFromTable('currentCourses', 'semesterID', this.state.semesters[i].semesterID).then(retrieve => {
              let success = retrieve.success;
              let data = retrieve.data;

              console.log('success: ' + success);
              return data;
            })
            this.setState({courses: this.state.courses.concat(response)});
      }
    }

    displayCourses(semesterID) {
      let array = [];
      for(let m = 0; m < this.state.courses.length; m++)
      {
        // console.log(semesterID);
        // console.log(this.state.courses[m].semesterID);
        if(semesterID == this.state.courses[m].semesterID)
        {
            array.push(
              <ul>
                <Link  onClick={(event) => { this.props.set({ courseID: this.state.courses[m].courseID, courseName: this.state.courses[m].courseName, semesterID: this.state.courses[m].semesterID  }) }}
                  to = {{
                    pathname: "/course",
                  }}>{this.state.courses[m].courseName}</Link>
              </ul>
            );
        }
      }
      return array;
    }
    
  

    render() {
      // console.log(this.state.semesters);
      // console.log(this.state.courses);
      return (
        <div className="semesters">
          <div className="container">
            <div className="row align-items-center my-5">
              <div className="col-lg-5">
                <h1 className="font-weight-light">Semesters</h1>
                <ul>
                  {this.state.semesters.map((semester) =>  (
                    <div>
                      <h4 key={semester.semesterID}>{semester.semesterName}</h4>
                      <ul className={'nav-item'} >
                      {this.displayCourses(semester.semesterID)}
                      </ul>
                    </div>
                  ))}
                </ul>
                
              </div>
            </div>
            </div>
            </div>
        );
    }
}

export default Semesters;

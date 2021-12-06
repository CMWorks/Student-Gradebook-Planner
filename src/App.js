import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import { Navigation, Footer, Home, Course, Login, Signup, Semesters, FinalGradeCalculator } from "./components";
import RESTModule from "./server/wpRESTModule";
import FutureCourse from "./components/FutureCourse";

class App extends React.Component {

  constructor(props) {
    super(props)
    this.server = new RESTModule();
    this.server.obj = "App"
    this.baseLocation = "/SGP/"
    this.state = {
      mode: "Login",
      user: {},
      courseID: -1,
      courseName: '',
      semesterID: '',
    }
  }

  render() {
    if (this.state.mode === "Entered") {
      return (
        <div className="App">
          <Router>
            <Navigation userData={this.state.user} server={this.server} set={(obj) => this.setState(obj)} baseLocation={this.baseLocation}/>
            <Switch>
              <Route path={this.baseLocation} exact component={() => <Home userData={this.state.user} server={this.server} set={(obj) => this.setState(obj)} />} />
              <Route path={this.baseLocation+"semesters"} exact component={() => <Semesters userData={this.state.user} server={this.server} set={(obj) => this.setState(obj)} baseLocation={this.baseLocation}/>} />
              <Route path={this.baseLocation+"future-courses"} exact component={() => <FutureCourse userData={this.state.user}server={this.server}set={(obj) => this.setState(obj)} />} />
              <Route path={this.baseLocation+"final-grade-calculator"} exact component={() => <FinalGradeCalculator />} />
              <Route path={this.baseLocation+"course"} exact component={() => <Course userData={this.state.user} courseID={this.state.courseID} courseName={this.state.courseName} semesterID={this.state.semesterID} server={this.server} set={(obj) => this.setState(obj) } />} />
            </Switch>
          </Router>
        </div>
      );
    } else if (this.state.mode === "Login") {
      // if (document.URL != this.baseLocation) {document.location = this.baseLocation}
      return (<div className="App"><Login server={this.server} set={(obj) => this.setState(obj)} /><Footer /></div>)
    } else {
      // if (document.URL != this.baseLocation) {document.location = this.baseLocation}
      return (<div className="App"><Signup server={this.server} set={(obj) => this.setState(obj)} /><Footer /></div>)
    }
  }
}

export default App;

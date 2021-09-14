import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import { Navigation, Footer, Home, About, Contact, Login, Signup } from "./components";
import serverModule from "./server/serverModule";

class App extends React.Component {

  constructor(props) {
    super(props)
    this.server = new serverModule();
    this.server.obj = "App"
    this.baseLocation = "http://localhost:3000/"
    this.state = {
      mode: "Login",
      user: {}
    }
  }

  /**
   * @abstract Sends updated user data to server and sets current user to updated user.
   * If the connection was unable to be made, then a new authorization token will be get.
   * If that does not work, then the system will reset
   * @param {*} data user data
   */
  updateUser(data) {
    this.setState({ user: data })
    this.server.updateUser(data.id, data).then((res) => {
      // authorizaiton token expired
      if (res.status === 401) {
        var eHash = this.server.generateHash(data.email, "")

        this.server.authenticate(eHash, data.userID).then((dataA) => {
          if (dataA.status === 401) {
            console.log("ERROR. UNABLE TO ACCESS TOKEN");
            this.setState({mode: "Login"})
          } else {
            this.server.token = dataA.access_token;
            this.server.myHeaders = {
              'Content-Type': 'application/json',
              'Authorization': ('Bearer ' + dataA.access_token)
            }
            this.updateUser(data)
          }
        })
      }
    })
  }

  render() {
    if (this.state.mode === "Entered") {
      return (
        <div className="App">
          <Router>
            <Navigation />
            <Switch>
              <Route path="/" exact component={() => <Home data={this.server.obj} set={(data) => this.updateUser(data)} />} />
              <Route path="/about" exact component={() => <About data={this.server.obj} set={(data) => this.updateUser(data)} />} />
              <Route path="/contact" exact component={() => <Contact data={this.server.obj} set={(data) => this.updateUser(data)} />} />
            </Switch>
            <Footer />
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
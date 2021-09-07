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

  setData(data) {
    this.server.obj = data
    console.log("SET DATA: " + data);
  }

  render() {
    if (this.state.mode === "Entered") {
      return (
        <div className="App">
          <Router>
            <Navigation />
            <Switch>
              <Route path="/" exact component={() => <Home data={this.server.obj} set={(data) => this.setData(data)} />} />
              <Route path="/about" exact component={() => <About data={this.server.obj} set={(data) => this.setData(data)} />} />
              <Route path="/contact" exact component={() => <Contact data={this.server.obj} set={(data) => this.setData(data)} />} />
            </Switch>
            <Footer />
          </Router>
        </div>
      );
    } else if (this.state.mode === "Login") {
      // if (document.URL != this.baseLocation) {document.location = this.baseLocation}
      return (<div className="App"><Login server={this.server} set={(obj) => this.setState(obj)}/><Footer /></div>)
    } else {
      // if (document.URL != this.baseLocation) {document.location = this.baseLocation}
      return (<div className="App"><Signup server={this.server} set={(obj) => this.setState(obj)}/><Footer /></div>)
    }
  }
}

export default App;
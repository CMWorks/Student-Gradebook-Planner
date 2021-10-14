import React from "react";

class Signup extends React.Component {

  constructor(props) {
    super(props);
    this.state = { firstName: '', lastName: '', email: '', password: '' };
    this.handleChangeEmail = this.handleChangeEmail.bind(this);
    this.handleChangePassword = this.handleChangePassword.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleChangeFName = this.handleChangeFName.bind(this);
    this.handleChangeLName = this.handleChangeLName.bind(this);
  }

  handleChangeFName(event) {
    this.setState({ firstName: event.target.value });
  }

  handleChangeLName(event) {
    this.setState({ lastName: event.target.value });
  }

  handleChangeEmail(event) {
    this.setState({ email: event.target.value });
  }

  handleChangePassword(event) {
    this.setState({ password: event.target.value });
  }

  handleSubmit(event) {
    // document.getElementById("nameInput").value = ""
    // document.getElementById("lastnameInput").value = ""
    // document.getElementById("emailInput").value = ""
    // document.getElementById("passwordInput").value = ""

    let userdata = {
      eHash: this.props.server.generateHash(this.state.email, ""),
      iHash: this.props.server.generateHash(this.state.email, this.state.password)
    }

    if (this.state.email === "" || this.state.password === "" || this.state.firstName === "" || this.state.lastName === "") {
      event.preventDefault();
      return
    }

    this.props.server.register(userdata).then((data) => {
      if (!data.success) {
        document.getElementById("emailInput").classList.add("is-invalid")
      } else {
        this.props.server.token = data.token;
        this.props.server.myHeaders = {
          'Content-Type': 'application/json',
          'Authorization': ('Bearer ' + data.token)
        }

        let User = {
          firstName: this.state.firstName,
          lastName: this.state.lastName,
          email: this.state.email,
          userID: userdata.iHash,
          semesters: []
        }

        this.props.server.addUserData('users', User.userID, User).then((dataBack) => {
          this.props.set({ mode: "Entered", user: dataBack })
        })
      }
    })

    event.preventDefault();
  }

  render() {
    return (
      <div className="signup">
        <div className="navigation">
          <nav className="navbar navbar-expand navbar-dark bg-dark">
            <div className="container">
              <h1 className="navbar-brand">Signup</h1>
              <div>
                <ul className="navbar-nav ml-auto">
                  <li className={`nav-item`}>
                    <label className="nav-link" onClick={(event) => { this.props.set({ mode: "Login" }) }}>
                      Login
                    </label>
                  </li>
                  <li className={`nav-item`}>
                    <label className="nav-link active">
                      Signup
                    </label>
                  </li>
                </ul>
              </div>
            </div>
          </nav>
        </div>
        <div className="container text-center py-5">
          <div className="row py-lg-5">
            <div className="col-lg-6 col-md-8 mx-auto">
              <h1>Signup</h1>
              <form className="form-floating needs-validation" id="inputForm" onSubmit={this.handleSubmit}>
                <div className="row g-3">
                  <div className="col-sm-6">
                    <label htmlFor="nameInput">First name</label>
                    <input type="text" className="form-control" id="nameInput" pattern="^[a-zA-Z]+-?[a-zA-Z0-9]+$" onChange={this.handleChangeFName} />
                  </div>
                  <div className="col-sm-6">
                    <label htmlFor="lastnameInput">Last name</label>
                    <input type="text" className="form-control" id="lastnameInput" pattern="^[a-zA-Z]+-?[a-zA-Z0-9]+$" onChange={this.handleChangeLName} />
                  </div>
                  <div className="col-12">
                    <label htmlFor="emailInput">Email address</label>
                    <input type="email" className="form-control" id="emailInput" aria-describedby="emailHelp" onChange={this.handleChangeEmail} />
                    <div className="invalid-feedback">Email already taken</div>
                  </div>
                  <div className="col-12">
                    <label htmlFor="passwordInput" className="form-label">Password</label>
                    <input type="password" className="form-control" id="passwordInput" onChange={this.handleChangePassword} />
                    <div className="invalid-feedback" v-show="errors.foo">Incorect email or password</div>
                  </div>
                  <div>
                    <button type="submit" className="btn btn-primary col-md-3">Submit</button>
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Signup;
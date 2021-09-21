import React from "react";

class Login extends React.Component {

  constructor(props) {
    super(props);
    this.state = { email: '', password: '' };
    this.handleChangeEmail = this.handleChangeEmail.bind(this);
    this.handleChangePassword = this.handleChangePassword.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChangeEmail(event) {
    this.setState({ email: event.target.value });
  }

  handleChangePassword(event) {
    this.setState({ password: event.target.value });
  }

  handleSubmit(event) {
    document.getElementById("emailInput").value = ""
    document.getElementById("passwordInput").value = ""

    var eHash = this.props.server.generateHash(this.state.email, "")
    var iHash = this.props.server.generateHash(this.state.email, this.state.password)

    this.props.server.authenticate(eHash, iHash).then((dataA) => {
      if (dataA.status === 401) {
        document.getElementById("passwordInput").classList.add("is-invalid")
        document.getElementById("emailInput").classList.add("is-invalid")
      } else {
        this.props.server.token = dataA.access_token;
        this.props.server.myHeaders = {
          'Content-Type': 'application/json',
          'Authorization': ('Bearer ' + dataA.access_token)
        }
        this.props.server.get(iHash).then((data) => {
          this.props.set({ mode: "Entered", user: data[0] })
        })
      }
    })

    event.preventDefault();
  }

  render() {
    return (
      <div className="login">
        <div className="navigation">
          <nav className="navbar navbar-expand navbar-dark bg-dark">
            <div className="container">
              <h1 className="navbar-brand">Login</h1>
              <div>
                <ul className="navbar-nav ml-auto">
                  <li className={`nav-item`}>
                    <label className="nav-link active">
                      Login
                    </label>
                  </li>
                  <li className={`nav-item`}>
                    <label className="nav-link" onClick={(event) => { this.props.set({ mode: "Signup" }) }}>
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
              <h1>Login</h1>
              <form className="form-floating" id="inputForm" onSubmit={this.handleSubmit}>
                <div className="mb-3">
                  <label htmlFor="emailInput">Email address</label>
                  <input type="email" className="form-control" id="emailInput" aria-describedby="emailHelp" onChange={this.handleChangeEmail} />
                </div>
                <div className="mb-3">
                  <label htmlFor="passwordInput" className="form-label">Password</label>
                  <input type="password" className="form-control" id="passwordInput" onChange={this.handleChangePassword} />
                  <div className="invalid-feedback">Incorect email or password</div>
                </div>
              </form>
              <div>
                <button className="btn btn-primary" onClick={this.handleSubmit}>Submit</button>
                {/* <button className="btn btn-secondary" style={{ 'marginLeft': '0px' }} onClick={(event) => { this.props.set({ mode: "Signup" }) }}>Login</button> */}
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Login;
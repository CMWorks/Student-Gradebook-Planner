// import React from "react";
import React, {useState} from "react";
import { Link, withRouter } from "react-router-dom";
import Popup from "./Popup";

function Navigation(props) {
  const [popUpButtonAccountOptions, setPopUpButtonAccountOptions] = useState(false);
  const [popUpButtonDeleteConfirmation, setPopUpButtonDeleteConfirmation] = useState(false);

  const [inFirstName, setInFirstName] = useState(props.userData.firstName);
  const [inLastName, setInLastName] = useState(props.userData.lastName);
  const [inEmail, setInEmail] = useState(props.userData.email);

  const handleChangeFName = (event) => {
    setInFirstName(event.target.value);
  }

  const handleChangeLName = (event) => {
    setInLastName(event.target.value);
  }

  const handleChangeEmail = (event) => {
    setInEmail(event.target.value);
  }

  const handleSubmitEditAccount = () => { 
    setPopUpButtonAccountOptions(false);
    props.userData.firstName = inFirstName;
    props.userData.lastName = inLastName;
    props.userData.email = inEmail;
    let id = props.userData.userID;
    props.server.updateUserData('users', id, props.userData);
    // console.log("Should submit account edits: " + props.userData.firstName + ", " + props.userData.lastName + ", " + props.userData.email);
  }

  const handleCancelEditAccount = () => {
    setPopUpButtonAccountOptions(false);
  }

  const handleSignOut = () => { 
    setPopUpButtonAccountOptions(false); 
    document.location.href = 'http://localhost:3000/'
    // console.log("Should sign out."); 
  }
  
  const handleDeleteAccount = () => {
    setPopUpButtonDeleteConfirmation(true);
  }

  const handleConfirmAccountDeletion = () => {
    setPopUpButtonDeleteConfirmation(false);
    setPopUpButtonAccountOptions(false);
    let id = props.userData.userID;
    props.server.deleteUserData('users', id);
    document.location.href = 'http://localhost:3000/';
    // console.log("Account should be deleted.");
  }

  const handleCancelAccountDeletion = () => {
    setPopUpButtonDeleteConfirmation(false);
  }
  
  return (
    <div className="navigation">
      <nav className="navbar navbar-expand navbar-dark bg-dark">
        <div className="container">
          <Link className="navbar-brand" to="/">
            {"Student Planner & Gradebook"}
          </Link>

          <Popup trigger={popUpButtonAccountOptions}>
            <h3>Account Options</h3>
            <div>
              <label>First name: </label>
              <input type="text" onChange={handleChangeFName} />
            </div>
            <div>
              <label>Last name: </label>
              <input type="text" onChange={handleChangeLName} />
            </div>
            <div>
              <label>Email: </label>
              <input type="text" onChange={handleChangeEmail} />
            </div>
            <div>
              <button style={{"marginRight": "10px", "marginTop": "10px"}} className="btn btn-primary" onClick={ () => {handleSubmitEditAccount()} }>
                Submit
              </button>
              <button style={{"marginTop":"10px"}} className="btn btn-primary" onClick={ () => {handleCancelEditAccount()} }>
                Cancel
              </button>
            </div>
            <div>
              <button style={{"marginTop":"30px"}} className="btn btn-primary" onClick={ () => {handleSignOut()} }>
                Sign Out
              </button>
            </div>
            <div>
              <button style={{"marginTop":"30px"}} className="btn btn-primary" onClick={ () => {handleDeleteAccount()} }>
                DELETE ACCOUNT
              </button>
            </div>
          </Popup>

          <Popup trigger={popUpButtonDeleteConfirmation}>
            <h3>Delete Account?</h3>
            <button style={{"marginRight":"10px"}} className="btn btn-primary" onClick={ () => {handleConfirmAccountDeletion()} }>
              Confirm
            </button>
            <button className="btn btn-primary" onClick={ () => {handleCancelAccountDeletion()}}>
              Cancel
            </button>
          </Popup>

          <div>
            <ul className="navbar-nav ml-auto">
              <li className={`nav-item`}>
                <Link className={'nav-link ' + (props.location.pathname === "/" ? "active" : "")} to="/">
                  Home
                  {/* <span className="sr-only">(current)</span> */}
                </Link>
              </li>
              <li className={`nav-item`}>
                <Link className={'nav-link ' + (props.location.pathname === "/about" ? "active" : "")} to="/about">
                  About
                </Link>
              </li>
              <li className={`nav-item`}>
                <Link className={'nav-link ' + (props.location.pathname === "/contact" ? "active" : "")} to="/contact">
                  Contact
                </Link>
              </li>
              <li className={`nav-item`}>
                <Link className={'nav-link ' + (props.location.pathname === "/semesters" ? "active" : "")} to="/semesters">
                  Semesters
                </Link>
              </li>
              <li className={'nav-item'}>
                <Link className={'nav-link ' + (props.location.pathname === "/final-grade-calculator" ? "active" : "")} to="/final-grade-calculator">
                  Final Grade Calculator
                </Link>
              </li>
              <li className={'nav-item'}>
                <button className="btn btn-primary" onClick={ () => {setPopUpButtonAccountOptions((true))} }>
                  Account
                </button>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </div>
  );
}

export default withRouter(Navigation);
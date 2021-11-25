// import React from "react";
import React, {useState} from "react";
import { Link, withRouter } from "react-router-dom";
import Popup from "./Popup";

function Navigation(props) {
  const [popUpButtonAccountOptions, setPopUpButtonAccountOptions] = useState(false);
  const [popUpButtonDeleteConfirmation, setPopUpButtonDeleteConfirmation] = useState(false);


  const handleSubmitEditAccount = () => {   // Needs to be finished.
    setPopUpButtonAccountOptions(false);
    console.log("Should submit account edits.");
  }

  const handleCancelEditAccount = () => {
    setPopUpButtonAccountOptions(false);
  }

  const handleSignOut = () => {   // Needs to be finished.
    setPopUpButtonAccountOptions(false); 
    console.log("Should sign out."); 
  }
  
  const handleDeleteAccount = () => {
    setPopUpButtonDeleteConfirmation(true);
  }

  const handleConfirmAccountDeletion = () => {  // Needs to be finished.
    setPopUpButtonDeleteConfirmation(false);
    setPopUpButtonAccountOptions(false);
    console.log("Account should be deleted.");
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
            <button style={{"marginRight":"10px"}} className="btn btn-primary" onClick={ () => {handleSubmitEditAccount()} }>
              Submit
            </button>
            <button style={{"marginRight":"10px"}} className="btn btn-primary" onClick={ () => {handleCancelEditAccount()} }>
              Cancel
            </button>
            <button style={{"marginRight":"10px"}} className="btn btn-primary" onClick={ () => {handleSignOut()} }>
              Sign Out
            </button>
            <button style={{"marginRight":"10px"}} className="btn btn-primary" onClick={ () => {handleDeleteAccount()} }>
              DELETE ACCOUNT
            </button>
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
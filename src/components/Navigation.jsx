// import React from "react";
import React, {useState} from "react";
import { Link, withRouter } from "react-router-dom";
import Popup from "./Popup";

function Navigation(props) {
  const [popUpButtonEditAccount, setPopUpButtonEditAccount] = useState(false);
  const [popUpButtonDeleteConfirmation, setPopUpButtonDeleteConfirmation] = useState(false);
  
  return (
    <div className="navigation">
      <nav className="navbar navbar-expand navbar-dark bg-dark">
        <div className="container">
          <Link className="navbar-brand" to="/">
            {"Student Planner & Gradebook"}
          </Link>

          <Popup trigger={popUpButtonEditAccount}>
            <h3>Edit Account</h3>
            <button style={{"marginRight":"10px"}} className="btn btn-primary" onClick={ () => {setPopUpButtonDeleteConfirmation(true)} }>
              DELETE ACCOUNT
            </button>
            <button style={{"marginRight":"10px"}} className="btn btn-primary" onClick={ () => {setPopUpButtonEditAccount(false); console.log("Submission to be sent.")} }>
              Submit
            </button>
            <button className="btn btn-primary" onClick={ () => {setPopUpButtonEditAccount((false))} }>
              Cancel
            </button>
          </Popup>

          <Popup trigger={popUpButtonDeleteConfirmation}>
            <h3>Delete Account?</h3>
            <button style={{"marginRight":"10px"}} className="btn btn-primary" onClick={ () => {setPopUpButtonDeleteConfirmation(false); setPopUpButtonEditAccount(false); console.log("Account to be deleted.")} }>
              Confirm
            </button>
            <button className="btn btn-primary" onClick={ () => {setPopUpButtonDeleteConfirmation(false)}}>
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
                <button className="btn btn-primary" onClick={ () => {setPopUpButtonEditAccount((true))} }>
                  Edit Account
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
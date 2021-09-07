import React from "react";
import { Link, withRouter } from "react-router-dom";

function Navigation(props) {
  return (
    <div className="navigation">
      <nav className="navbar navbar-expand navbar-dark bg-dark">
        <div className="container">
          <Link className="navbar-brand" to="/">
            {"Student Planner & Gradebook"}
          </Link>

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
            </ul>
          </div>
        </div>
      </nav>
    </div>
  );
}

export default withRouter(Navigation);
import React from "react";
import { NavLink } from 'react-router-dom'
import { BLOG, HOME, COURSE, LOGIN, DAFTAR } from "../../constant";
import { Nav, Navbar } from "react-bootstrap";

const Navig = () => {
  return (
    <Navbar collapseOnSelect expand="sm" className="navbar navbar-expand-lg navbar-light">
      <div className="container">
        <Navbar.Brand>
          <a href={HOME}>
            <img
              className='img50'
              src="https://metalit.oss-ap-southeast-5.aliyuncs.com/static/metalit/assets/images/Group_38_1.png"
            />
          </a>
        </Navbar.Brand>

        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse id="responsive-navbar-nav">
          <Nav className="navbar-nav ms-auto mb-2 mb-lg-0">
            <Nav.Link className="nav-item text-uppercase px-3" href={COURSE}>Pelatihan</Nav.Link>
            <Nav.Link className="nav-item text-uppercase px-3" href={BLOG}>Blog</Nav.Link>
            <Nav.Link className="nav-item text-uppercase px-3" href={LOGIN}>Login</Nav.Link>
            <Nav.Link className="nav-item text-uppercase px-3" href={DAFTAR}>Daftar</Nav.Link>
          </Nav>
        </Navbar.Collapse>
        </div>
      </Navbar>
    );
  };

export default Navig;
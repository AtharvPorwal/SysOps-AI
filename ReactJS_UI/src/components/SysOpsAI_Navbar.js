import React from "react";
import logo from "../image/logo.jpg";
class SysOpsAI_Navbar extends React.Component {
  state = {};
  render() {
    return (
      <nav className="navbar " style={{ backgroundColor: "rgb(52, 52, 52)" }}>
        <div className="container-fluid">
          <a
            className="navbar-brand"
            href="#"
            style={{ color: "rgb(243, 243, 243)" }}
          >
            <img
              src={logo}
              alt="Logo"
              style={{
                width: "40px",
                height: "40px",
                marginRight: "10px",
                borderRadius: "50%",
              }}
            />
            SysOps AI
          </a>
        </div>
      </nav>
    );
  }
}

export default SysOpsAI_Navbar;

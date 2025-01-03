import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Form, Button, Navbar } from "react-bootstrap";
import "./login.css";
import "../App.css";
import SysOpsAI_Navbar from "./SysOpsAI_Navbar";

const Login = () => {
  const [inputUsername] = useState("admin");
  const [inputPassword] = useState("admin");

  const navigate = useNavigate();

  //   const [loading, setLoading] = useState(false);

  const handleSubmit = async (event) => {
    //   event.preventDefault();
    //   setLoading(true);
    //   await delay(500);
    //   console.log(Username:${inputUsername}, Password :${inputPassword});
    if (inputUsername == "admin" && inputPassword == "admin") {
      navigate("/dashboard");
    } else {
      alert("Try again");
    }
    // setLoading(false);
  };

  //   const handlePassword = () => {};

  //   function delay(ms) {
  //     return new Promise((resolve) => setTimeout(resolve, ms));
  //   }

  return (
    <>
      <SysOpsAI_Navbar />
      <div className="sign-in__wrapper">
        <div className="sign-in__backdrop"></div>
        <Form className="shadow p-4 bg-white rounded">
          <div className="h4 mb-2 text-center">Sign In</div>
          <Form.Group className="mb-2" controlId="username">
            <Form.Label>Username</Form.Label>
            <Form.Control type="text" placeholder="Username" required />
          </Form.Group>
          <Form.Group className="mb-2" controlId="password">
            <Form.Label>Password</Form.Label>
            <Form.Control type="password" placeholder="Password" required />
          </Form.Group>
          <Button
            className="w-100"
            variant="primary"
            type="submit"
            onClick={handleSubmit}
            style={{ backgroundColor: "rgb(52, 52, 52)" }}
          >
            Log In
          </Button>
        </Form>
      </div>
    </>
  );
};

export default Login;
